from collections import deque

order, size = map(int, input().split())  # размер графа
graph = {v : {} for v in range(order)}


def add_edge(graph, v1, v2, weight):  # функция для добавления ребра в граф
    graph[v1][v2] = weight
        

def create_graph():  # функция для создания графа
    for _ in range(size):
        v1, v2, weight = map(int, input().split())
        add_edge(graph, v1, v2, weight)
        add_edge(graph, v2, v1, weight)


def dijkstra(graph, start):  # стандартный алгоритм Дейкстра
    queue = deque([start])
    distances = dict()
    distances[start] = 0
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if (neigh_v not in distances
                or 
                distances[cur_v] + graph[cur_v][neigh_v] < distances[neigh_v]
               ):
                distances[neigh_v] = distances[cur_v] + graph[cur_v][neigh_v]
                queue.append(neigh_v)
    return distances


create_graph()
dist_sum = []
for v in graph:  # для каждой вершины считаем сумму расстояний от других вершин до нее
    dist_sum.append(sum(dijkstra(graph, v).values()))
    
print(dist_sum.index(min(dist_sum)))  # столицей будет тот город, до которого сумма расстояний минимальна