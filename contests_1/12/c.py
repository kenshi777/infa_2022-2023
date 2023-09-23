def prefix(s):
    pi = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        p = pi[i - 1]
        while p > 0 and s[i] != s[p]:
            p = pi[p - 1]
        if s[i] == s[p]:
            p += 1
        pi[i] = p
    return pi

s = input()

print(*prefix(s))