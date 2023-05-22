list = []
max_num = 0
while True:
    a = int(input())
    list.append(a)
    if a == 0:
        max_num = list[0]
        for i in range(len(list)):
            if max_num < list[i]:
                max_num = list[i]
        print(max_num)
        break