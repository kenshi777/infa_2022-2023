n = int(input())
a = []
b = []
s = 0
for i in range(n):
    a.append(input())

for i in a:
    for j in i:
        s += int(j)
    b.append(s)
    s = 0
for i in range(n-1):
    for j in range(1, n-i):
        if b[j-1] > b[j]:
            b[j-1], b[j] = b[j], b[j-1]
            a[j-1], a[j] = a[j], a[j-1]
        elif b[j] == b[j-1] and int(a[j-1]) > int(a[j]):
            b[j-1], b[j] = b[j], b[j-1]
            a[j-1], a[j] = a[j], a[j-1]
for i in a:
    print(i)

