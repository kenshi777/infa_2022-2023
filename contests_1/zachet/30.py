def kuzya(n):
    C = [0] * (n+1)
    C[1] = 1
    for i in range(2, n+1):
        C[i] = C[i-1] + C[i-2]
    return C[-1]

print(kuzya(4))