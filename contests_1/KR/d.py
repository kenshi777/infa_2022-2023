l = []
n_1 = 0
n_4 = 0
while True:
    a = input()
    if a == '#':
        break
    else:
        a = int(a)
        l.append(a)
lenghth = len(l)

for i in range(lenghth):
    n_1 += l[i]
n_1 = n_1 / lenghth

n_2 = max(l)
n_3 = min(l)

for i in range(0, lenghth-2, 3):
    n_4 += ((l[i] + l[i+1] + l[i+2]) % l[i+2])

print(round(n_1, 3),n_2,n_3,n_4)