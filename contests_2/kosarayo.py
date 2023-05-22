N, M = map(int, input().split())

G = {}
G_inv = {}
for _ in range(M):
    v1, v2 = input().split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
            G_inv[v] = []
    G[v1].append(v2)
    G_inv[v2].append(v1)

print(G)

def dfs(G, vertex, used, stack):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used, stack)
    stack.append(vertex)

used = set()
stack = []
for vertex in G.keys():
    if vertex not in used:
        dfs(G, vertex, used, stack)

N = 0
used = set()
while len(stack) > 0:
    v = stack.pop()
    if v not in used:
        componenta = []
        dfs(G_inv, v, used, componenta)
        print(componenta)
        N += 1

print(N)
