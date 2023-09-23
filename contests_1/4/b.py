a = int(input())
i = 2
flag = False

while i < a:
    if a % i != 0:
        i += 1
    else:
        flag = True
        break

if flag: print(0)
else: print(1)
    