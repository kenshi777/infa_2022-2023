a = [1, 2, 3, 14, 41, 23, 41, 25, 41, 40, 14]
m = a[0]
k = 1
for i in range(len(a)):
    if a[i] > m:
        m = a[i]
        k = 1
    elif a[i] == m:
        k += 1

print(m, k)