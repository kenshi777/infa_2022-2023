def insert_sort(A):
    '''Вставками типо вставляет число в уже отсортированный массив, меняя справа налево пока не воткнемся'''
    n = len(A)
    for i in range(n):
        k = i
        while k > 0 and A[k-1] > A[k]:
            A[k-1], A[k] = A[k], A[k-1]
            k -= 1

    return A

print(insert_sort([5, 4, 3, 2, 1]))