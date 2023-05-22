G = {}

for i in 'abcdefgh':
    for j in '12345678':
        G[i+j] = set()

for x in G:
    for y in G:
        if abs((ord(x[0]) - ord(y[0])) * (ord(x[1]) - ord(y[1]))) == 2:
            G[x].add(y)
            G[y].add(x)

for i in G:
    print('\''+str(i)+'\'', ':', G[i], ',')