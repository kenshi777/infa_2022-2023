a = int(input())
b = int(input())
c = int(input())

list = [a, b, c]
list_1 = [a, b, c]
d = max(list)
list_1.remove(max(list))

if (list_1[0] + list_1[1] > d):
    if d**2 < (list_1[0]**2 + list_1[1]**2):
        print("acute")
    elif d**2 > (list_1[0]**2 + list_1[1]**2):
        print("obtuse")
    else:
        print("right")
else:
    print("impossible")