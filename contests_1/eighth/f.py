flag = True
l = input().split()

for i in range(2):
    l[i] = int(l[i])

M = input().split()
N = input().split()

for i in range(l[0]):
    M[i] = int(M[i])
for i in range(l[1]):
    N[i] = int(N[i])

for i in M:
    if N.count(i) == 0:
        flag = False
        break

for i in N:
    if M.count(i) == 0:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')
