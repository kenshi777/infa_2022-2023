s = input()
l = len(s)
integ = []
i = 0
sum = 1
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
 
for i in range(len(integ)):
    sum *= integ[i]

print(sum)