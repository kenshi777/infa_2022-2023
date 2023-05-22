num = int(input())

l = len(str(num))

list = []
s = 0
for i in range(l):
    if len(str(num)) != 1:
        k = num % 10
        num = str(num)
        num = num[:(len(num)-1)]
        num = int(num)
        list.append(k)
    else:
        list.append(num)
list.reverse()

for i in range(len(list)):
    s+=list[i]*((-10)**(len(list)-(i+1)))

print(s)
