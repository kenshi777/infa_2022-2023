num = input().split()
list =[]
sum_loc = 0
sum_glob = 0

for i in range(len(num)):
    for j in range(len(num[i])):
        if num[i][j] == '.':
            sum_loc += 1
        elif num[i][j] == '|':
            sum_loc += 5
    list.append(sum_loc)
    sum_loc = 0

for i in range(len(list)):
    sum_glob += list[i]*(20**(len(list) - i - 1))

print(sum_glob)