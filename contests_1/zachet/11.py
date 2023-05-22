n = int(input())
d = 2
sosik = []
while n != 1:
    if n % d == 0:
        n /= d
        sosik.append(d)
    else:
        d += 1

print(sosik)