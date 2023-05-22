s = [int(i) for i in input().split()]
s.sort()
r = [0 for i in range(110)]
r[0] = r[1] = s[1] - s[0]

for i in range(2, len(s)):
    r[i] = min(r[i - 1] + s[i] - s[i - 1], r[i - 2] + (s[i] - s[i - 1]))

print(r[len(s) - 1])