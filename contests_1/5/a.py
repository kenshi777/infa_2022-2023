count = 0
l = int(input())
list = []
for i in range(l):
    list.append(int(input()))
index = int(input())

for i in list:
    if i > list[index]:
        count += 1

print(count)

