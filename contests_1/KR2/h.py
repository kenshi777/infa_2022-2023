s = input()

x, y = ord(s[0]) - ord('a'), int(s[1]) - 1
p = list(list(0 for _ in range(8)) for _ in range(8))
p[0][0] = 1

for i in range(8):
    for j in range(8):
        if sorted((abs(x - i), abs(y - j))) == [1, 2] or (i == x and j == y):
            continue
        if i > 0:
            p[i][j] += p[i - 1][j]
        if j > 0:
            p[i][j] += p[i][j - 1]
        if i > 0 and j > 0:
            p[i][j] += p[i - 1][j - 1]
print(p[7][7])