n = int(input())

l = [i for i in range(n+1)]

l[1] = 0

i = 2

while i < n**0.5:
    if l[i] != 0:
        j = i*2
        while j <= n:
            l[j] = 0
            j += i
    i += 1

a = set(l)
a.remove(0)

print(*a)
