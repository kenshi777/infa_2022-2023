hash_table = [[] for i in range(10)]
def polynom_hash(base, module, s):
    polynom = 0
    for i in range(len(s)):
        polynom += ord(s[i]) * base ** (len(s)-i-1)
    hash = polynom % module
    return hash
# def insert(key, value):
#     hash = polynom_hash(91, 100, key)
#     if hash_table[hash%10] == []:
#         hash_table[hash%10].append([hash, key, value])
#     else:
#         for i in range(len(hash_table[hash%10])):
#             if hash_table[hash%10][i][1] == key:
#                 hash_table[hash%10][i][2] = value
#                 break
#             else:
#                 hash_table[hash%10].append([hash, key, value])
#     return 

def insert(key, value):
    h = polynom_hash(91, 100, key)
    num = h % 10 #номер строки в таблице
    flag = 0
    if len(hash_table[num]) != 0:
        for i in range(0, len(hash_table[num])):
            if hash_table[num][i][1] == key:
                hash_table[num][i][2] = value
                flag = 1
    if flag == 0:
        hash_table[num].append([h, key, value])
    return

n = int(input())
for i in range(n):
    key, value = input().split()
    insert(key, value)

for i in range(10):
    if hash_table[i] != []:
        print(i)
        for j in range(len(hash_table[i])):
            print(*hash_table[i][j])