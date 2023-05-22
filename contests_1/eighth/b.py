def merge(L, R):
    S = [0]*(len(L)+len(R))
    i = 0
    k = 0
    n = 0
    while i < len(L) and k < len(R):
        if L[i] <= R[k]:
            S[n] = L[i]
            i += 1
            n += 1
        else:
            S[n] = R[k]
            k += 1
            n += 1
    while i < len(L):
        S[n] = L[i]
        i += 1
        n += 1
    while k < len(R):
        S[n] = R[k]
        k += 1
        n += 1
    return S
def merge_sort(A, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A)  #  состояние переменных при вызове
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L, depth + 1, part='left')
    merge_sort(R, depth +1, part='right')
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A)  # состояние переменных перед выходом из функции
    #  если функция не вызвала сама себя, состояние переменных перед выходом из функции не должно выводиться,
    #      поскольку гарантированно известно, что массив A в таком случае не изменяется
merge_sort([2, 4, 1, 3, 2, 10])