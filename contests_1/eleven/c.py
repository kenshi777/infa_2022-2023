def chess(W, B):
    C = [[0] * 9 for i in range(9)]
    C[W[0]][W[1]] = 1
    for i in range(W[0]+1, 9):
        for j in range(1,9):
            if B[i][j]:
                if j == 8:
                    C[i][j] = C[i-1][j-1]
                elif j == 1:
                    C[i][j] = C[i-1][j+1]
                else:    
                    C[i][j] = C[i-1][j-1] + C[i-1][j+1]
            else:
                C[i][j] = C[i-1][j]
    if W[0] == 8:
        return [1]
    else: return C[-1]

B = [[False] * 9 for i in range(9)]

d = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
}

n = int(input())
for i in range(n):
    c = input()
    B[int(c[1])][d[c[0]]] = True

w = input()
W = [0, 0]
W[1] = d[w[0]]
W[0] = int(w[1])

res = chess(W, B)
s = 0
for i in range(len(res)):
    s += res[i]

print(s)
