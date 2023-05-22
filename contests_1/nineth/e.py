def bubble_sort2d(matrix, N, M):
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end=' ')
        print()
    print()
    len_n = N*M
    for bypass in range(1, len_n):
        for k in range(0, len_n - bypass):
            if matrix[k // M][k % M] > matrix[(k + 1) // M][(k + 1) % M]:
                matrix[k // M][k % M], matrix[(k + 1) // M][(k + 1) % M] = matrix[(k + 1) // M][(k + 1) % M], matrix[k // M][k % M]
                for i in range(N):
                    for j in range(M):
                        print(matrix[i][j], end=' ')
                    print()
                print()