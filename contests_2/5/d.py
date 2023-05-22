x1, y1, x2, y2 = map(float, input().split())
xa, ya = map(float, input().split())

if x1 != x2 and y1 != y2:
    n = (y2 - y1) / (x2 - x1)
    x0 = (xa - n * y1 + n ** 2 * x1 + n * ya) / (n ** 2 + 1)
    y0 = y1 + n * (x0 - x1)
else:
    if x1 == x2:
        x0 = x1
        y0 = ya
    if y1 == y2:
        x0 = xa
        y0 = y1

xb = 2 * x0 - xa
yb = 2 * y0 - ya

print(round(xb, 5), round(yb, 5))