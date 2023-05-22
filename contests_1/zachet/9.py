a = [1, 2, 3, 14, 23, 25, 41, 40, 14]
m = a[0]
k = 0
for i in range(len(a)):
    if a[i] > m:
        m = a[i]
        k = i
print(m, k)