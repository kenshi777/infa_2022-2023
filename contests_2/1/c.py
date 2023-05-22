n = input()
l = []
N = int(n)
s=''
for i in range(len(n)):
    l.append(N % 10)
    N //= 10
l = l[::-1]

for i in range(len(n)):
    s += f'{l[i]}*10^{len(n)-1-i} + '

print(s[:len(s)-3])