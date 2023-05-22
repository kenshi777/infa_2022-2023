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
    k = 0
    for x in L+M+R:
        A[k] = x
        k += 1
    return A

print(hoar_sort([7, 4, 5, 2, 2, 5, 2, 3, 10, 2]))