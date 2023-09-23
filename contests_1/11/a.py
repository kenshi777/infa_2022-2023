def checker(x, y):
    desk = [[0]*8 for i in range(8)]
    desk[y-1][x-1] = 1
    for i in range(y, 8):
        for j in range(8):
            if j == 0:
                desk[i][j] = desk[i - 1][j + 1]
            elif j == 7:
                desk[i][j] = desk[i - 1][j - 1]
            else:
                desk[i][j] = desk[i - 1][j + 1] + desk[i - 1][j - 1]
    return desk[7]

s = input().split()
m, n = int(s[0]), int(s[1])

total = checker(m, n)
count = 0

for i in total:
    count += i

print(count)