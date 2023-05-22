used = list()
G = dict()
cur_comp = list()

def dfs(v):
    cur_comp.append(v)
    used.append(v)
    for uw in G[v]:
        if uw[0] not in used:
            dfs(uw[0])
    return


n, m = [int(x) for x in input().split()]
for i in range(n):
    G[i] = set()
matr = [[0] * n for x in range(n)]
for i in range(0, m):
    u, v, w = [int(x) for x in input().split()]
    G[u].add((v, w))
    G[v].add((u, w))
    matr[u][v] = w
ans = list()
for uw in G:
    if len(used) == n:
        break
    if uw not in used:
        dfs(uw)
        ans.append(0)
        for i in cur_comp:
            for j in cur_comp:
                ans[len(ans) - 1] += matr[i][j]
        cur_comp = list()
ans = sorted(ans)
for x in ans:
    print(x)