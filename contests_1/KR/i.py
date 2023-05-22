l = []
s = ''
N = int(input())
for i in range(N):
    l.append(input().split())
for i in range(N):
    s = ''
    for j in range(N):
        s = s + l[j][i]+' '

    print(s[:-1])
