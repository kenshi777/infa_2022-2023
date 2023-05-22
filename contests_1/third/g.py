num = int(input())
list_num = []
list_vav = []
str_=''

while num != 0:
    remains = num % 60
    num = num // 60
    list_num.append(remains)

for i in range(len(list_num)):
    if list_num[i] < 10:
        r = list_num[i]
        d = 0
    else:
        r = list_num[i] % 10
        d = list_num[i] // 10
    list_vav.append('<'*d + 'v'*r)

if len(list_vav) == 1:
    print(list_vav[0])
else:
    list_vav.reverse()
    for i in range(len(list_vav)):
        str_+=list_vav[i]+'.'
    print(str_[:len(str_)-1])