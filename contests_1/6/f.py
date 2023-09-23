a = [int(x) for x in input().split()]
lst = [list() for _ in range(2)]
n = len(a)
c = len(str(max(a)))

for i in range(c):
    for x in a:
        lst[x // (10 ** i) % 10].append(x)
    a.clear()
    for l in lst:
        for x in l:
            a.append(x)
        l.clear()
    print(*a)