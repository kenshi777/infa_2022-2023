def backpack(N, M, m, v):
    '''Задача о рюкзаке m - массы, v - стоимости'''
    F = [[0]*(N + 1) for i in range(M + 1)]
    for i in range(1, N + 1):
        for k in range(1, M + 1):
            if m[i] <= k:
                F[k][i] = max(F[k][i-1], v[i] + F[k-m[i]][i-1])
            else:
                F[k][i] = F[k][i-1]
    return F[M][N]