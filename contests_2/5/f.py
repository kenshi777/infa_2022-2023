
n = int(input())
lines = dict()
for i in range(0, n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if y == 0:
        a = float(0)
        b = float(1)
        if x > 0:
            direction = 1
        if x < 0:
            direction = 2
    else:
        a = float(1)
        b = - x / y
        if x >= 0:
            direction = 1
        else:
            direction = 2
    line = tuple([a, b, direction])
    if line in lines:
        lines[line] += 1
    else:
        lines[line] = 1

print(max(lines.values()))