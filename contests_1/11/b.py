def attraction(N, M, Price):
    INF = 10 ** 20
    C = [[0] * (M + 1) for i in range(N + 1)]
    C[0][0] = 0
    for i in range(1, N + 1):
        C[i][0] = INF
    for j in range(1, M + 1):
        C[0][j] = INF
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                C[i][j] = min(C[i][j - 1], C[i - 1][j], C[i-1][j-1]) + Price[i][j]
            else:
                C[i][j] = min(C[i][j - 1], C[i - 1][j]) + Price[i][j]
    return C[-1][-1]

M = int(input())
N = int(input())
Price = [[0] * (N + 1) for i in range(M+1)]
for i in range(1, M+1):
    for j in range(1, N+1):
        Price[i][j] = int(input())

S = int(input())

C = attraction(M, N, Price)

if S - C >= 0:
    print(S-C)
else: print('Impossible')



