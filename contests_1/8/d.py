def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)
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
    hoar_sort(L, depth + 1, part='left')
    hoar_sort(R, depth + 1, part='right')
    for i in range(len(L+M+R)):
        A[i] = (L+M+R)[i]

    print('depth:', depth, 'part:', part, 'array after:', A)

hoar_sort([5, 2, 4, 8, 7, 1, 3, 10, 6])