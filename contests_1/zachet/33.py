def lcs(A, B):
    C = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i] == B[j]:
                C[i][j] = 1 + C[i-1][j-1]
            else:
                C[i][j] = max(C[i-1][j], C[i][j-1])
    return C[-1][-1]