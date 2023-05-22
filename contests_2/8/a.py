from collections import deque

order, size, start, finish = map(int, input().split())  # размеры графа, стартовая и конечная вершины
graph = dict()


def add_edge(graph, v1, v2, weight):  # функция добавления ребра в граф
    if v1 not in graph:  # если вершины еще нет в графе, добавляем ее и взвешенное ребро
        graph[v1] = {v2 : weight}
    else:  # если вершина уже есть в графе, то добавляем в список взвешенное ребро
        graph[v1][v2] = weight
        

def create_graph():  # функция для считывания неориентированного графа
    for _ in range(size):  # считывание ввода
        v1, v2, weight = map(int, input().split())
        add_edge(graph, v1, v2, weight)  # добавление соответствующих ребер и вершин в граф
        add_edge(graph, v2, v1, weight)


def dijkstra(graph, start):  # стандартный алгоритм Дейкстра
    queue = deque([start])  # очередь для вершин
    distances = dict()  # список минимальных расстояний до вершин от вершины start
    distances[start] = 0  # расстояние до самой точки start равно нулю
    while queue:  # пока очередь не опустела, продолжаем обход
        cur_v = queue.popleft()  # текущая вершина - верхняя из очереди
        for neigh_v in graph[cur_v]:  # проверяем ее соседей
            if (neigh_v not in distances  # если соседняя вершина еще не посещена или
                or                        # уже записанное расстояние до нее больше чем соответствуюшее 
                distances[cur_v] + graph[cur_v][neigh_v] < distances[neigh_v] # значение при проходе по ребру,
               ):  # то обновляем значение на новое меньшее
                distances[neigh_v] = distances[cur_v] + graph[cur_v][neigh_v]
                queue.append(neigh_v)  # и добавляем вершину в очередь
    return distances


def min_path(graph, start, finish):  # функция для поиска минимального пути из вершины start в вершину finish
    distances = dijkstra(graph, start)  # список минимальных расстояний от вершины start
    cur_v = finish  # идем от вершины finish
    min_path = [finish]  # нужный путь (написанный наоборот)
    while cur_v != start:  # продолжаем путь, пока не придем в вершину start
        for neigh_v in graph[cur_v]:
            # проверяем для соседних вершин, равно ли записанное для них расстояние сумме расстояния от
            if distances[cur_v] == distances[neigh_v] + graph[neigh_v][cur_v]:  # текущей вершины и веса ребра
                min_path.append(neigh_v)  # если это выполнено, то вершина - часть минимального пути
                cur_v = neigh_v  # меняем текущую вершину
                break  # выходим из цикла по соседним вершинам
    return min_path[::-1]  # возвращаем нужный путь


create_graph()
print(*min_path(graph, start, finish))