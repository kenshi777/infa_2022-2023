a1, b1, c1 = map(float, input().split())
a2, b2, c2 = map(float, input().split())

d = a1 * b2 - b1 * a2

if d == 0:
    print('NO')
else:
    d1 = -c1 * b2 + c2 * b1
    d2 = -a1 * c2 + a2 * c1
    print(round(d1 / d), round(d2 / d))