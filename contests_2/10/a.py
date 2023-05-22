n = int(input())
m = [0] * (n+1)
m[0] = 1
if n == 1:
    print(1)
else:
    m[1] = m[2] = 0

    for i in range(3, n+1):
        if i % 3 == 0:
            s = m[i-1] + m[i-2]
            if s > 0:
                m[i] = 0
            else:
                m[i] = 1
        elif i % 3 == 1:
            s = m[i-1] + m[i-3]
            if s > 0:
                m[i] = 0
            else:
                m[i] = 1
        else:
            s = m[i-1] + m[i-2] + m[i-3]
            if s > 0:
                m[i] = 0
            else:
                m[i] = 1

    print(2 if m[n] == 1 else 1)
    #if (m[n]== 1) printf("2\n") else printf("1\n")