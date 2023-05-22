n = input()
s = 0
N = int(n)
for i in range(len(n)):
    s += N % 10
    N //= 10

print(s)

