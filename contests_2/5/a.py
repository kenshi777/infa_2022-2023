x1, y1, r1 = list(map(int, input().split()))
x2, y2, r2 = list(map(int, input().split()))

if min(abs(r1 - r2), abs(r2 - r1)) <= pow((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1), 0.5) <= r1 + r2:
    print('YES')
elif x1 == x2 and y1 == y2 and r1 == r2:
    print('YES')
else:
    print('NO')
