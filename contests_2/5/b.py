gopher = list(map(int, input().split()))
dog = list(map(int, input().split()))
holes = []
n = int(input())
for i in range(n):
    holes.append(list(map(int, input().split())))
n = -1
flag = False
for i in range(len(holes)):
    l_gopher = (gopher[0] - holes[i][0]) ** 2 + (gopher[1] - holes[i][1]) ** 2
    l_dog = (dog[0] - holes[i][0]) ** 2 + (dog[1] - holes[i][1]) ** 2
    if l_dog < 4 * l_gopher:
        continue
    else:
        flag = True
        n = i+1
        break

print(n if flag else -1)