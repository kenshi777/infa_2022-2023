list = []
list_full=[]
sum_ = 0
while True:
    a = int(input())
    list.append(a)
    if a == 0:
        for i in range(len(list)-1):
            if list[i] % 2 != 0:
                list_full.append(list[i+1])
        if list_full == [] or len(list_full) < 2:
            print(-1)
        else:
            for j in range(len(list_full)):
                sum_ += list_full[j]
            print(sum_)
        break