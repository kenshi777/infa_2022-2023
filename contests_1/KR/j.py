N = int(input())
l = [0] * 10
f = []
L = []
for i in range(N):
    a = input()
    if a not in f:
        f.append(a)
    l[f.index(a)] += 1

for i in range(len(f)):
    L.append([l[i],f[i]])

L = sorted(L)[::-1]
for i in range(len(L)):
    print(L[i][1], L[i][0])



    

