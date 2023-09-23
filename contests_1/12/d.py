def z_function(s):
    z = [0 for _ in range(len(s))]
    l = 0
    r = 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

s = input()
print(*z_function(s))