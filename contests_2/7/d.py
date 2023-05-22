n, m = map(int, input().split())
table = [list(map(int, input().split())) for q in range(n)]


# Т.к. нам надо от чего-то отталкиваться, то преподготовим и заполним всю таблицу 
# расстоянием -1(можно вырать любое другое отрицательное число)

dist = [[-1 for _ in range(m)] for q in range(n)]
list1 = []

# Находим клетки с единицами и добавляем их в список
for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            dist[i][j] = 0
            list1.append((i, j))

# Используем алгоритм BFS
# (динамическое программирование с ассимптотикой o(n^3) работает(идея на семинаре), но слишком медленно,
# т.к  BFS работает за o(m*n)

# Цикл пока не опустеет list1, т.е. пока не пробежим все значения, где значение вершинки == 1 
while list1:
    i, j = list1[0]
    # Удаляем использованный элемент
    del list1[0]
    # Проверка сверху снизу слева и справа
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1:
            dist[ni][nj] = dist[i][j] + 1
            list1.append((ni, nj))

# принт результата
for i in dist:
    print(" ".join(map(str, i)))