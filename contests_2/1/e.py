def dot_product(N, vector1, vector2):
    s = 0
    for i in range(N):
        s += vector1[i]*vector2[i]
    return s

print(dot_product(3, [1, 2, 3], [1, 2, 3]))