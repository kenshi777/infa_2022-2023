a = [int(x) for x in input().split()]
b = [x for x in range(10)]
c = [0]*10
n = len(a)
s=""
for i in range(n):
    for j in range(10):
        if a[i] == b[j]:
            c[j] += 1
    print(*c)
for i in range(len(c)):
    if c[i] != 0:
        s += c[i]*str(b[i])
print(*s)