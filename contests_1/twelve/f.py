def z_func(s):
    z = [0] * len(s)
    l = int(0)
    r = int(0)
    for i in range(1, len(s)):
        k = int(0)
        if i < r:
            k = min(r - i, z[i - l])
        while (i + k < len(s) and s[i + k] == s[k]):
            k += 1
        z[i] = k
        if (i + z[i] > r):
            l = i
            r = i + z[i]
    return z

s = input()
s += s[::-1]
z = (z_func(s)[::-1])[:int(len(s) / 2)]
for i in range(0, len(z)):
    print(z[i], end = " ")