n = int(input()) # кол-во мостов
a = [[int(j) for j in input().split()] for i in range(n)] # считываем матрицу смежности
null = input()
res = 0
color = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            if color[i] != color[j]:
                res += 1
res = res // 2
print(res)