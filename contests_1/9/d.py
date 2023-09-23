def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    for i in range(len(L+M+R)):
        A[i] = (L+M+R)[i]
    return A

S_1 = 0
S_2 = 0
N = int(input())
L = list(map(int, input().split()))
hoar_sort(L)

for i in range((N // 2), N):
    S_1 += L[i]

for i in range(N // 2):
    S_2 += L[i]

print(S_1 - S_2)
