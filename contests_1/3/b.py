n = int(input())
list = []
temp = []
stat_age = 60
delta_weight = 10
sum_ = 0

for i in range(n):
    str_ = input().split()
    list.append(str_)

for i in range(n):
    if (not ((int(list[i][1]) - 100)-delta_weight <= int(list[i][2]) <= (int(list[i][1]) - 100)+delta_weight)) or (int(list[i][0]) >= 60):
        temp.append(float(list[i][3]))
if len(temp) != 0:
    for i in range(len(temp)):
        sum_ += temp[i]

    print(sum_ / len(temp))
else:
    print(0)

