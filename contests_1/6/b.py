a = [int(x) for x in input().split()]
n = len(a)
for i in range(1,n):
    while i != 0 and a[i] < a[i-1]:
        a[i], a[i-1] = a[i-1], a[i]
        print(*a)
        i -= 1