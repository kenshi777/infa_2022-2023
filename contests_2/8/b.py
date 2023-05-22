order, size, start = map(int, input().split())  # размеры графа и стартовая вершина для обхода

edges = []  # список ребер (взвешенных)
for _ in range(size):
    edges.append(list(map(int, input().split())))

distances = [10**10] * order  # инициализируем расстояния большими числами
distances[start] = 0  # расстояние до стартовой точки равно нулю

for _ in range(order - 1):  # итерируемся по допустимому числу ребер в составе пути
    for v1, v2, weight in edges:  # для каждого ребра из списка
        if (distances[v1] != 10**10  # если вершина уже посещена 
            and                      # и расстояние, записанное для 2 вершины, больше значения,
            distances[v2] > distances[v1] + weight  # получаемое для этого ребра,
           ):                                       # то записываем меньшее значение
            distances[v2] = distances[v1] + weight
            
for v1, v2, weight in edges:  # если вершина посещена, но расстояние при проходе по 
    if (distances[v1] != 10**10  # ребру увеличивается, то это отрицательный цикл
        and
        distances[v2] > distances[v1] + weight
       ):
        distances[v2] = -10**10  # помечаем такие вершины
        
for i in range(len(distances)):  # если это непосещенная вершина или вершины
    if (abs(distances[i]) >= 10**10):  # в отрицательном цикле, то помечаем ее
        distances[i] = 'UDF'  # как неопределенную
        
print(*distances)