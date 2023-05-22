def counting_sort(A):
    n = len(A)
    B = [0]*(len(A)+1)
    for i in A:
        B[i] += 1
    C = []
    for i in range(1, n):
        C += [i]*B[i]
    return C, B

print(counting_sort([1, 2, 1, 4, 4, 3, 3, 3, 9, 8, 8,7]))