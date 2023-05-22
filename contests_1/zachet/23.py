def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

print(left_bound([2, 2, 2, 2, 3, 4, 5, 5, 7, 10], 4))