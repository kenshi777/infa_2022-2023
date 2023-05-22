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
    distances = {v: float('+inf') for v in G}
    q = Queue()
    q.put(start)
    distances[start] = 0
    
    while not q.empty():
        v = q.get()
        for neighbour in G[v]:
            if distances[neighbour] == float('+inf'):
                q.put(neighbour)
                distances[neighbour] = distances[v] +1
    return distances

def path(G, start, end):
    distances = bfs(G, start)
    res = [end]
    while distances[end] != 0:
        for v in G[end]:
            if distances[end] - distances[v] == 1:
                end = v
                res.append(end)
                break
    return res[::-1]

dist = bfs(G, 'A')
print(G)
print(path(G, 'A', 'J'))