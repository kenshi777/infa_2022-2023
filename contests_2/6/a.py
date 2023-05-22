n = int(input())
m = []

for i in range(n):
    m.append(list(map(int, input().split())))

flag = False
for i in range(n):
    for j in range(n):
        if m[i][j] != m[j][i]:
            flag = True

print('NO' if flag else 'YES')