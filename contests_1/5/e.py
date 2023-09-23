N = int(input())
l = input().split()
extr = []
for i in range(N):
    l[i] = int(l[i])

for i in range(1, N-1):
    if (l[i-1] < l[i] and l[i] > l[i+1]) or (l[i-1] > l[i] and l[i] < l[i+1]):
        extr.append(i)

print(*extr)

