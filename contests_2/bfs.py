from queue import Queue

N, M = map(int, input().split())

G = {}
for _ in range(M):
    v1, v2 = input().split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)

def bfs(G, vertex, used=None):
    N = 0
    if used is None:
        used = set()
    q = Queue()
    q.put(vertex)
    while not q.empty():
        v = q.get()
        if v not in used:
            N += 1
            used.add(v)
            print('{} is {} vertex'.format(v, N))
            for neighbour in G[v]:
                q.put(neighbour)

used = set()

for v in G.keys():
    if v not in used:
        bfs(G, v, used)