def findSmallest(s,n):
    if s > 9 * n or s < n and n - 1 :
        print("impossible")
        return
    res=[1 for i in range(n+1)]
    s -= 1 * n
    i = n - 1
    while s and i + 1 :
        if s > 9 :
            res[i] = 9
            s -= 8
        else :
            res[i] += s 
            s = 0
        i -= 1
    for i in range(n) :
        print(res[i], end="")
 
a, b = map(int,input().split())
findSmallest(a, b)



