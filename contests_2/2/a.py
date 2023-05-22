base, module = list(map(int, input().split()))
s = input()

polynom = 0

for i in range(len(s)):
    polynom += ord(s[i]) * base ** (len(s)-i-1)

hash = polynom % module
print(hash)