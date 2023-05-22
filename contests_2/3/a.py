from collections import deque
s = input().split()
d = deque()
c = 0
d.append(s[0])
for i in range(1, len(s)):
    if len(d) < 2:
        d.append(s[i])
        continue
    elif d[len(d)-1][0] == d[len(d)-2][0] and abs(int(d[len(d)-1][1]) - int(d[len(d)-2][1])):
        c += 2
        d.popleft()
        d.popleft()
        if len(d) > 1 and d[0][0] == d[len(d)-1][0]:
            c += 2
            d.pop()
            d.popleft()
    d.append(s[i])

print(c)


