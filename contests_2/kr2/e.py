from collections import deque

# считываем размер поля и координаты начальной и конечной клеток
n, m = map(int, input().split())
start_row, start_col = map(int, input().split())
end_row, end_col = map(int, input().split())

# считываем поле
field = [input() for _ in range(n)]

# инициализируем массив расстояний
distances = [[float('inf')] * m for _ in range(n)]
distances[start_row][start_col] = 0

# создаем очередь и добавляем в нее начальную клетку
queue = deque([(start_row, start_col)])

# запускаем алгоритм BFS
while queue:
    row, col = queue.popleft()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < m and field[new_row][new_col] != 'X' and distances[new_row][new_col] == float('inf'):
            distances[new_row][new_col] = distances[row][col] + 1
            queue.append((new_row, new_col))

# выводим результат
if distances[end_row][end_col] == float('inf'):
    print("INF")
else:
    print(distances[end_row][end_col])