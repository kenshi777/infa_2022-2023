list = []
min_num = 0
count = 0
while True:
    a = int(input())
    list.append(a)
    if a == 0:
        min_num = list[0]
        for i in range(len(list)-1):
            if min_num > list[i]:
                min_num = list[i]
        for j in range(len(list)-1):
            if list[j] == min_num:
                count = count + 1
        print(count)
        break