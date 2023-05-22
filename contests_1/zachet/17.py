def choice_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(i, n-1):
            if A[i] > A[j+1]:
                A[i], A[j+1] = A[j+1], A[i]
    return A

print(choice_sort([5, 4, 3, 2, 1]))