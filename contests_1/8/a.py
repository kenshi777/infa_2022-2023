def merge(L, R):
    S = [0]*(len(L)+len(R))
    i = 0
    k = 0
    n = 0
    while i < len(L) and k < len(R):
        if L[i] <= R[k]:
            S[n] = L[i]
            i += 1
            n += 1
        else:
            S[n] = R[k]
            k += 1
            n += 1
    while i < len(L):
        S[n] = L[i]
        i += 1
        n += 1
    while k < len(R):
        S[n] = R[k]
        k += 1
        n += 1
    return S

print(merge([1, 3, 100], [7, 2, 5]))


