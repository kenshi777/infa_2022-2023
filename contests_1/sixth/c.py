a = [int(x) for x in input().split()]
n = len(a)
while not all(a[i] <= a[i+1] for i in range(n - 1)):
    for i in range(1, n):
        if a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            print(*a)
            break

