A = [12, 5, 664, 63, 5, 73, 93, 127, 432, 64, 34]

n = len(str(max(A)))
rang = 10

for i in range(n):
    B = [[] for i in range(rang)]
    for x in A:
        figure = x // 10**i % 10
        B[figure].append(x)
    A = []
    for k in range(rang):
        A += B[k]

print(A)
