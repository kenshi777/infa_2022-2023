N = int(input()) + 1
st=''
A = [True for i in range(N)]
A[0] = A[1] = False
for i in range(N):
    if A[i] == True:
        for j in range(i+i, N, i):
            A[j] = False

res = []
for i in range(N):
    if A[i]:
        res.append(i)

for i in res:
    st = st + str(i) + " "
print(st[:-1])