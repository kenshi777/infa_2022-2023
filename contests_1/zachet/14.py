b = [1, 2, 3, 4, 5]
a = 2
n = len(b)

for i in range(n-a):
    b.append(b[0])
    del b[0]

print(b)