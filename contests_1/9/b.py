def left_bound(A, key, right, left):
        if right - left <= 1:
            return left
        else:
            middle = (left + right) // 2
            if A[middle] < key:
                left = middle
                return left_bound(A, key, right, left)
            else:
                right = middle
                return left_bound(A, key, right, left)

def right_bound(A, key, right, left):
        if right - left <= 1:
            return right
        else:
            middle = (left + right) // 2
            if A[middle] <= key:
                left = middle
                return right_bound(A, key, right, left)
            else:
                right = middle
                return right_bound(A, key, right, left)

N = input()
S = list(map(int, N.split()))
K = int(input())

if right_bound(S, K, len(S), -1)-left_bound(S, K, len(S), -1) > 1:
    print(left_bound(S, K, len(S), -1)+2)
else:
    print(-1)