list = []
sum_= 0
while True:
    a = int(input())
    list.append(a)
    if a == 0:
        for i in range(len(list)):
            sum_ += list[i]
        print(sum_)
        break


