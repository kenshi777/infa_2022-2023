def lcs(s1, s2):
    F = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
    for i in range(1, len(s1) +1):
        for j in range(1, len(s2)):
            if s1[i-1] == s2[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    print(F)
    L = []
    i = len(s1)
    j = len(s2)
    while i != 0 and j != 0:
        if F[i - 1][j -1] - F[i][j] == 1 and s1[i - 1] == s2[j - 1]:
            print('ok')
            L.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if F[i - 1][j] == F[i][j]:
                i -= 1
            else:
                j -= 1
    return L[::-1]

print(lcs([1, 5, 7, 8, 9, 2, 4, 6], [3, 6, 7, 5, 7, 6, 1, 2]))