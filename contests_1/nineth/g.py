def bubble_sort_first_num(A):
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k][0] > A[k+1][0]:
                A[k], A[k+1] = A[k+1], A[k]

N = int(input())
P = []
for i in range(N):
    M = int(input())
    for j in range(M):
        P.append(input())

for i in range(len(P)):
    P[i] = P[i].split()

for i in range(len(P)):
    P[i][0] = float(P[i][0])

bubble_sort_first_num(P)
P = P[::-1]

print(len(P))
for i in range(len(P)):
    print(str(format(P[i][0], '.2f'))+' '+P[i][1])
