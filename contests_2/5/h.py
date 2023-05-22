class point():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


def orient_square_triangle(O, point1, point2):
    return ((point1.x - O.x) * (point2.y - O.y) - (point1.y - O.y) * (point2.x - O.x)) / 2


def square(polygon):
    O = point(0, 0)
    SS = 0
    for i in range(1, len(polygon)):
        SS += orient_square_triangle(O, polygon[i - 1], polygon[i])
    return abs(SS)


s = input().split()
polygon = list()
ans = list()
while s[0] != "end":
    if s[0] == "add":
        pos = int(s[1])
        x = float(s[2])
        y = float(s[3])
        polygon.insert(pos, point(x, y))
    else:
        polygon.append(polygon[0])
        ans.append(square(polygon))
        polygon.pop()
    s = input().split()

for x in ans:
    print(round(x, 5))