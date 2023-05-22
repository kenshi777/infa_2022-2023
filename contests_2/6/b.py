n = int(input())
m = []

for i in range(n):
    m.append(list(map(int, input().split())))

l = []
for i in range(n):
    for j in range(n):
        if m[i][j] == 0:
            continue
        print(i, j, m[i][j])