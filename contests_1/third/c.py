num = int(input())
str_=""

l = len(str(num))

list = []

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
for i in range(l):
    str_ += f"{list[i]}*10^{len(list)-1-i} + "
str_ = str_[:(len(str_)-3)]

print(str_)
