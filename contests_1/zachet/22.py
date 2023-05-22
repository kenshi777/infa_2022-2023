def merge(A, B):
    C = [0]*(len(A)+len(B))
    i=0
    k=0
    n=0
    while i<len(A) and k<len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = A[:middle]
    R = A[middle:]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    k = 0
    for x in C:
        A[k] = x
        k += 1
    return A

print(merge_sort([7, 4, 5, 2, 2, 5, 2, 3, 10, 2]))
