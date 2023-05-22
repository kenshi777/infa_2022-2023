l = []
for i in range(4):
    a = int(input())
    l.append(a)

if abs(l[0] - l[2]) == abs(l[1]-l[3]) or l[0] == l[2] or l[1] == l[3]:
    print('YES')
else:
    print('NO')
