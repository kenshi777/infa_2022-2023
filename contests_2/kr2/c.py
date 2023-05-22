G = dict()
n, m = [int(i) for i in input().split()] #n - количество вершин, m - количество ребер, x, y - начальная и конечная вершины
x = 0
for i in range(0, n):
    G[i] = set()
for i in range(0, m):
    a, b = [int(j) for j in input().split()]
    G[a].add(b)
    G[b].add(a)
used = [False] * n
used[x] = True
d = [0] * n
qeue = []
qeue.append(x)
while len(qeue) > 0:
    v = qeue[0]
    qeue.pop(0)
    for u in G[v]:
        if used[u] == False:
            qeue.append(u)
            used[u] = True
            d[u] = d[v] + 1
for x in d:
    print(x)