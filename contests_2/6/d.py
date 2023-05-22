def read_graph(M):
    G = {}  # граф, со стрелочками в правильную сторону
    for i in range(M):
        v1, v2 = list(map(int, input().split()))
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
    return G


def dfs(G, vertex, used, stack, path):  # used - вершины, по которым мы прошлись, vertex - вершина, с которой начинаем, G - граф
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            path.append(v)
            dfs(G, v, used, stack, path)  # то есть мы пробегаемся по всем вершинам и зовем всех соседей на дискотеку,
            # если они еще не позваны, когда всех соседей позвали, то и сами соглашаемся
    # после того как мы всех позвали, добавляем себя в стек
    path.pop(len(path)-1)
    if len(G[vertex]) > 0 and -1 not in stack and len(path) > 0:
        # print(path)
        for v1 in G[vertex]:
            if v1 in path:
                path.append(vertex)
                stack.append(-1)
                stack.extend(path[path.index(v1):])
                stack.append(-1)
                break

n, m = list(map(int, input().split())) # n - число вершин, m - число ребер

flag = False

G = read_graph(m)
used = set() #список используемых вершин
stack = []
path = []
for vertex in G.keys():
    if vertex not in used and not flag:
        path.append(vertex)
        dfs(G, vertex, used, stack, path)
        if -1 in stack:
            flag = True
            break

start_cycle = -1
end_cycle = -1

# print(stack)

if not flag:
    print('YES')
else:
    for i in range(len(stack)):
        if stack[i] == -1 and start_cycle == -1:
            start_cycle = i
        elif stack[i] == -1 and end_cycle == -1:
            end_cycle = i
            break
    print(*stack[start_cycle + 1:end_cycle])