a = int(input())
Flag = False
for i in range(14):
    if a == 2**i:
        Flag = True
if Flag: print('YES')
else: print('NO')