def point_in_polygon(polygon, point):
    # Находим минимальную и максимальную координаты по оси X среди вершин многоугольника
    min_x = min(p[0] for p in polygon)
    max_x = max(p[0] for p in polygon)
    
    # Если координата X точки находится вне диапазона [минимальная координата X, максимальная координата X],
    # то точка не может находиться внутри многоугольника
    if point[0] < min_x or point[0] > max_x:
        return 'NO'
    
    # Находим точку на границе многоугольника, которая находится на луче, исходящем из данной точки вправо
    intersections = 0
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i+1)%len(polygon)]
        # Проверяем, пересекает ли ребро многоугольника луч, исходящий из данной точки вправо
        if (p1[1] > point[1]) != (p2[1] > point[1]) and \
           point[0] < (p2[0] - p1[0]) * (point[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
            intersections += 1
    
    # Если количество пересечений нечетное, то точка находится внутри многоугольника, иначе - снаружи
    if intersections % 2 == 1:
        return 'YES'
    else:
        return 'NO'

n = int(input())
polygon = []
for i in range(n):
    polygon.append(list(map(float, input().split())))

point = list(map(float, input().split()))

print(point_in_polygon(polygon, point))