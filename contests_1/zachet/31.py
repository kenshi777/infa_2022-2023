def kuzya(A):
    n = len(A)
    C = [0]*(n+1)
    C[1] = A[0]
    for i in range(2, n+1):
        C[i] = min(C[i-2], C[i-1]) + A[i-1]
    
    cur_index = n
    path = []
    while cur_index > 0:
        if C[cur_index] - A[cur_index-1] == C[cur_index - 1]:
            cur_index -= 1
            path.append(cur_index)
        else:
            cur_index -= 2
            path.append(cur_index)
    return C[-1], path

print(kuzya([0, 1, 2, 100, 1000, 5, 7, 100]))