N = 187
e = 3
d = 107
l = list(int(a) for a in input().split())
dec = [0]*len(l)

for i in range(len(l)):
    dec[i] = (l[i] ** d) % N

print(*dec)