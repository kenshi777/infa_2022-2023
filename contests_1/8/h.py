def bubble_sort(A):
    N = len(A)
    for bypass in range(1,N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]