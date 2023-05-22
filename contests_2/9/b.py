def is_loop(graph):  # функция для проверки, есть ли цикл в графе
                     # если есть, то сортировка невозможна
        
    def dfs(vertex, graph, color):
        color[vertex] = 1
        for neighbour in graph[vertex]:
            if color[neighbour] == 0:
                if dfs(neighbour, graph, color):
                    return True
            elif color[neighbour] == 1:
                return True
        color[vertex] = 2
        return False


    color = [0] * order

    for vertex in graph:
        if dfs(vertex, graph, color):
            return True
    return False

    
order, size = map(int, input().split())
graph = {v : set() for v in range(order)}

for _ in range(size):
    v1, v2 = map(int, input().split())
    graph[v1-1].add(v2-1)
    
if is_loop(graph):
    print('No')
else:
    print('Yes')