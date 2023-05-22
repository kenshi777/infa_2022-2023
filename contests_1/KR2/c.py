s = input()
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = {}

for j in alph:
    count.update({j:0})

for i in s:
    if i.isalpha():
        count[i] += 1

for i in alph:
    if count[i] != 0:
        print(i, count[i])