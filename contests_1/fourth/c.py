a = int(input())
i = 2
factorise = []

while i <= a:
    if a % i != 0:
        i += 1
    else:
        a = a / i
        factorise.append(i)
        i = 2

for j in range(len(factorise)):
    print(factorise[j])
