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
A = []
first_not_zero = 0
N = input()
for i in N:
    A.append(int(i))

hoar_sort(A)

for i in range(len(A)):
    if A[i] != 0:
        first_not_zero = i
        break

if first_not_zero == 0:
    print(*A, sep='')
else:
    A[0], A[first_not_zero] = A[first_not_zero], A[0]
    print(*A, sep='')