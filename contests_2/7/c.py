from collections import deque

order, size = map(int, input().split())  # наш граф
graph = {v : set() for v in range(order)}
for _ in range(size):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)


def bfs(start_v):  # функция для поиска в ширину
    if graph[start_v]:  # если из вершины не выходят ребра, то пропускаем ее
        parents = [None] * order  # список предков вершин
        distances = [None] * order  # расстояния (здесь не очень нужны)
        distances[start_v] = 0
        queue = deque([start_v])  # очередь для записи вершин
        while queue:
            cur_v = queue.popleft()  # текущая вершина
            for neighbour_v in graph[cur_v]:
                if distances[neighbour_v] is None:  # если вершина не посещена, добавляем ее в 
                    distances[neighbour_v] = distances[cur_v] + 1  # соответствующие списки
                    parents[neighbour_v] = cur_v
                    queue.append(neighbour_v)
                elif neighbour_v == start_v:  # если мы вернулись в изначальную вершину, то это
                    path = [cur_v]  # значит, что мы нашли кратчайший цикл с ней
                    parent = parents[cur_v]
                    while not parent is None:  # сохраняем цикл
                        path.append(parent)
                        parent = parents[parent]
                    return path[::-1]
    return []


cycles = []
for start_v in graph:  # запускаем обход в ширину из каждой вершины
    cycle = bfs(start_v)
    if cycle:  # сохраняем все кратчайшие циклы
        cycles.append(cycle)

if not cycles:  # если циклов нет, то их нет =)
    print('NO CYCLES')
    exit(0)
else:  # иначе сортируем их по длине, выбираем минимальный
    cycles.sort(key=len)
    print(*cycles[0])