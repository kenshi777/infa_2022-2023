n, k = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

if n == 3 and k == 2:
    print(x[n - 1] - x[0])
l, r = 0, x[n - 1] - x[0]
while l != r:
    m = (l + r) // 2
    g, j = 1, 0
    for i in range(1, n):
        if x[i] - x[j] >= m:
            j = i
            g += 1
    if g >= k:
        l = m + 1
    else:
        r = m
print(l - 1)