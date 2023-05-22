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

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right

N = int(input())
K = int(input())
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

if right_bound(A, K)-left_bound(A, K) > 1:
    print(left_bound(A, K)+2)
else:
    print(-1)
