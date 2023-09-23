def step(x0, y0, x2, y2):
    if x0 + 2 <= 8 and  x1 == x0 + 2 and ((y1 == y0 + 1 and y0 + 1 <= 8) or (y1 == y0 - 1 and y0 -1 >= 1)):
        return True
    if x0 + 1 <= 8 and x1 == x0 + 1 and ((y1 == y0 + 2 and y0 + 2 <= 8) or (y1 == y0 - 2 and y0 - 2 >= 1)):
        return True
    if x0 - 2 >= 1 and x1 == x0 - 2 and ((y1 == y0 + 1 and y0 + 1 <= 8) or (y1 == y0 - 1 and y0 - 1 >= 1)):
        return True
    if x0 - 1 >=1 and x1 == x0 - 1 and ((y1 == y0 + 2 and y0 + 2 <= 8) or (y1 == y0 - 2 and y0 - 2 >= 1)):
        return True
    return False


def ans(x0, y0, x2, y2):
    if x0 == x1 and y0 == y1:
        return 0
    if step(x0, y0, x2, y2):
        return 1
    if ((x0 + 2 <= 8 and y0 + 1 <= 8 and step(x0 + 2, y0 + 1, x2, y2)) or
            (x0 + 2 <= 8 and y0 - 1 >= 1 and step(x0 + 2, y0 - 1, x2, y2)) or
            (x0 + 1 <= 8 and y0 + 2 <= 8 and step(x0 + 1, y0 + 2, x2, y2)) or
            (x0 + 1 <= 8 and y0 - 2 >= 1 and step(x0 + 1, y0 - 2, x2, y2)) or
            (x0 - 2 >= 1 and y0 + 1 <= 8 and step(x0 - 2, y0 + 1, x2, y2)) or
            (x0 - 2 >= 1 and y0 - 1 >= 1 and step(x0 - 2, y0 - 1, x2, y2)) or
            (x0 - 1 >= 1 and y0 + 2 <= 8 and step(x0 - 1, y0 + 2, x2, y2)) or
            (x0 - 1 >= 1 and y0 - 2 >= 1 and step(x0 - 1, y0 - 2, x2, y2))):
        return 2
    return -1

x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())
print(ans(x0, y0, x1, y1))
