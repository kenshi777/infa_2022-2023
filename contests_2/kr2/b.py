n, m = map(int, input().split())
edges = [[] for _ in range(n)]
degrees = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    degrees[a] += 1
    degrees[b] += 1

regular = True
for d in degrees:
    if d != degrees[0]:
        regular = False
        break

if regular:
    print("YES")
else:
    print("NO")