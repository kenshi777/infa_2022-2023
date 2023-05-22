n = int(input())
groups = input().split()
for i in range(n):
    groups[i] = int(groups[i])

def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    for i in range(len(L+M+R)):
        A[i] = (L+M+R)[i]
    return A

hoar_sort(groups)

people = 0

for i in range(len(groups)//2 + 1):
    if groups[i] == 0:
        people += 0
    else:
        people += groups[i] // 2 + 1

print(people)



