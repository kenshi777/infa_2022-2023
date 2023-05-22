def split_barrier(A, barrier):
    for x in A:
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
    for i in range(len(L+M+R)):
        A[i] = (L+M+R)[i]

A = [3, 4, 2, 0, 6, 6]
split_barrier(A, 3)
print(A)