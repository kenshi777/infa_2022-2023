n = int(input())
count = 2
j = 1

while j <= n:
    isprime = True
    
    for x in range(2, count):
        if count % x == 0: 
            isprime = False
            break
    
    if isprime:
        j += 1
    
    count += 1

print(count-1)


