m = []
s = 0
N = int(input())
for i in range(N):
    a = input().split()
    for j in range(N):
        a[j] = int(a[j])
    m.append(a)

for i in range(N):
    s += m[i][i]

print(s) 
