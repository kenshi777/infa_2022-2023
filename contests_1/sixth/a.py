a = [int(x) for x in input().split()]
n = len(a)
for i in range(n-1):
    c = i
    for j in range(i+1, n):
        if a[j] < a[c]:
            c = j
    if a[i] > a[c]: 
        a[i], a[c] = a[c], a[i]
        print(*a)

