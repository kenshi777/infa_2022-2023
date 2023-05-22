from collections import deque

graph = {'a1' : {'b3', 'c2'} ,
'a2' : {'c3', 'c1', 'b4'} ,
'a3' : {'b5', 'c4', 'c2', 'b1'} ,
'a4' : {'c3', 'b2', 'c5', 'b6'} ,
'a5' : {'b3', 'c4', 'c6', 'b7'} ,
'a6' : {'b8', 'c5', 'c7', 'b4'} ,
'a7' : {'b5', 'c8', 'c6'} ,
'a8' : {'b6', 'c7'} ,
'b1' : {'c3', 'a3', 'd2'} ,
'b2' : {'c4', 'd3', 'a4', 'd1'} ,
'b3' : {'d2', 'd4', 'c1', 'a5', 'a1', 'c5'} ,
'b4' : {'d3', 'c2', 'c6', 'a6', 'a2', 'd5'} ,
'b5' : {'a7', 'd6', 'd4', 'c7', 'c3', 'a3'} ,
'b6' : {'d7', 'c4', 'a8', 'a4', 'c8', 'd5'} ,
'b7' : {'c5', 'd8', 'd6', 'a5'} ,
'b8' : {'a6', 'c6', 'd7'} ,
'c1' : {'b3', 'a2', 'e2', 'd3'} ,
'c2' : {'e1', 'd4', 'e3', 'b4', 'a1', 'a3'} ,
'c3' : {'e2', 'b1', 'b5', 'e4', 'a4', 'd1', 'a2', 'd5'} ,
'c4' : {'d2', 'b6', 'd6', 'e3', 'b2', 'a5', 'e5', 'a3'} ,
'c5' : {'b3', 'd3', 'd7', 'b7', 'e4', 'a6', 'a4', 'e6'} ,
'c6' : {'e7', 'a7', 'd4', 'b4', 'a5', 'b8', 'e5', 'd8'} ,
'c7' : {'e8', 'b5', 'a8', 'a6', 'd5', 'e6'} ,
'c8' : {'e7', 'a7', 'd6', 'b6'} ,
'd1' : {'c3', 'b2', 'f2', 'e3'} ,
'd2' : {'b3', 'b1', 'e4', 'c4', 'f3', 'f1'} ,
'd3' : {'f4', 'e1', 'f2', 'b2', 'c1', 'b4', 'e5', 'c5'} ,
'd4' : {'b3', 'e2', 'c2', 'b5', 'c6', 'f5', 'f3', 'e6'} ,
'd5' : {'e7', 'f4', 'b6', 'f6', 'e3', 'c7', 'b4', 'c3'} ,
'd6' : {'b7', 'b5', 'e4', 'c4', 'e8', 'f5', 'f7', 'c8'} ,
'd7' : {'b6', 'f6', 'b8', 'e5', 'f8', 'c5'} ,
'd8' : {'f7', 'c6', 'e6', 'b7'} ,
'e1' : {'f3', 'd3', 'c2', 'g2'} ,
'e2' : {'g3', 'f4', 'd4', 'c1', 'c3', 'g1'} ,
'e3' : {'c2', 'c4', 'f5', 'g2', 'f1', 'd1', 'd5', 'g4'} ,
'e4' : {'d2', 'g3', 'f2', 'g5', 'f6', 'c3', 'c5', 'd6'} ,
'e5' : {'d3', 'd7', 'c4', 'c6', 'g6', 'f3', 'f7', 'g4'} ,
'e6' : {'f4', 'g7', 'g5', 'd4', 'c7', 'd8', 'f8', 'c5'} ,
'e7' : {'g8', 'c6', 'f5', 'g6', 'c8', 'd5'} ,
'e8' : {'g7', 'c7', 'd6', 'f6'} ,
'f1' : {'d2', 'g3', 'h2', 'e3'} ,
'f2' : {'h3', 'd3', 'e4', 'h1', 'd1', 'g4'} ,
'f3' : {'d2', 'h4', 'e1', 'g5', 'h2', 'd4', 'g1', 'e5'} ,
'f4' : {'e2', 'd3', 'g2', 'h5', 'g6', 'h3', 'd5', 'e6'} ,
'f5' : {'h4', 'e7', 'g3', 'g7', 'd4', 'e3', 'h6', 'd6'} ,
'f6' : {'g8', 'd7', 'e8', 'e4', 'h5', 'h7', 'd5', 'g4'} ,
'f7' : {'g5', 'e5', 'h6', 'h8', 'd8', 'd6'} ,
'f8' : {'h7', 'd7', 'e6', 'g6'} ,
'g1' : {'f3', 'e2', 'h3'} ,
'g2' : {'e3', 'f4', 'e1', 'h4'} ,
'g3' : {'e2', 'e4', 'f5', 'h5', 'h1', 'f1'} ,
'g4' : {'f2', 'h2', 'f6', 'e3', 'e5', 'h6'} ,
'g5' : {'e4', 'f3', 'f7', 'h3', 'h7', 'e6'} ,
'g6' : {'h4', 'e7', 'f4', 'e5', 'h8', 'f8'} ,
'g7' : {'f5', 'h5', 'e6', 'e8'} ,
'g8' : {'e7', 'h6', 'f6'} ,
'h1' : {'g3', 'f2'} ,
'h2' : {'f3', 'f1', 'g4'} ,
'h3' : {'g1', 'f4', 'f2', 'g5'} ,
'h4' : {'f3', 'f5', 'g2', 'g6'} ,
'h5' : {'g3', 'f4', 'g7', 'f6'} ,
'h6' : {'g4', 'g8', 'f7', 'f5'} ,
'h7' : {'f8', 'g5', 'f6'} ,
'h8' : {'f7', 'g6'}}

red, green = input().split()  # исходные точки красного и зеленого коней

distances_red = {v: None for v in graph}
distances_red[red] = 0
distances_green = {v: None for v in graph}
distances_green[green] = 0

queue_red = deque([red])
queue_green = deque([green])


def bfs(start_v, queue, distances):  # поиск в ширину
    while queue:  # пока очередь не очистилась, считаем расстояние между каждой вершиной,
        cur_v = queue.popleft()  # соединенной каким-либом путем со стартовой, и стартовой вершиной
        for neighbour_v in graph[cur_v]:
            if distances[neighbour_v] is None:
                distances[neighbour_v] = distances[cur_v] + 1
                queue.append(neighbour_v)

            
bfs(red, queue_red, distances_red)
bfs(green, queue_green, distances_green)

min_dist = []
for vertex in graph:  # если для какой-то вершины расстояния совпали, то записываем их
    if distances_green[vertex] == distances_red[vertex]:
        min_dist.append(distances_green[vertex])
        
if min_dist:  # если это множество непусто, печатаем минимальное расстояние
    print(min(min_dist))
else:  # если пусто, то кони не могут встретиться
    print(-1)