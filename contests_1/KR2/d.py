def mas(mol):
    mas = 0
    i = 0
    while i < len(mol):
        k = 1
        if i != len(mol) - 1 and mol[i + 1].isdigit():
            k = int(mol[i + 1])

        if mol[i] == 'C':
            mas += 12 * k
        elif mol[i] == 'N':
            mas += 14 * k
        elif mol[i] == 'O':
            mas += 16 * k
        else:
            mas += k
        i += 1
        if k != 1:
            i += 1
    return mas

def merge_by_molweight(L, R):
    S = [0]*(len(L) + len(R))
    i = j = k = 0
    while i < len(L) and j < (len(R)):
        if mas(L[i]) <= mas(R[j]):
            S[k] = L[i]
            i += 1
        else:
            S[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        S[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        S[k] = R[j]
        j += 1
        k += 1
    return S

print(merge_by_molweight(['H2', 'CH4', 'C2H5OH'], ['O2', 'NO2']))