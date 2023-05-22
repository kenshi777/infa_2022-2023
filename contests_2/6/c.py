n = int(input())
m = int(input())
p = []
for i in range(m):
    p.append(list(map(int,input().split())))

graph = {i:[] for i in range(n)}
for elem in p:
    if graph.get ( elem[0], 0 ) == 0:
        graph [elem[0]] = []
    graph [elem[0]].append (elem[1])


def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return(visited)

flag = False

for key in graph.keys():
    visited=set()
    dfs(visited, graph, key)
    if len(visited) != len(graph):
        flag = True

print('NO' if flag else 'YES')