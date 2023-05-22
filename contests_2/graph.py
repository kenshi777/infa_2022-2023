N, M = map(int, input().split())

G = {}
for _ in range(M):
    v1, v2 = input().split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)

print(G)

def dfs(G, vertex, used=None):
    if used is None:
        used = set()
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used)

N = 0
used = set()
for vertex in G.keys():
    if vertex not in used:
        dfs(G, vertex, used)
        N += 1