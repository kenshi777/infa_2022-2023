def levenstain(A, B):
    C = [[(i+j) if (i*j) == 0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if A[i] == B[j]:
                C[i][j] = C[i-1][j-1]
            else:
                C[i][j] = 1 + min(C[i][j-1], C[i-1][j], C[i-1][j-1])
    return C[len(A)][len(B)]
