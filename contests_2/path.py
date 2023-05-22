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

def bfs(G, start):
    path = {v: None for v in G}
    q = Queue()
    q.put(start)
    path[start] = ['A']
    
    while not q.empty():
        v = q.get()
        for neighbour in G[v]:
            if path[neighbour] is None:
                q.put(neighbour)
                path[neighbour] = path[v] + [neighbour]
    return path

print(bfs(G, 'A'))