n, k = map(int, input().split()) 
s = [int(x)%(k+1) for x in input().split()] 
a = s[0] 
for i in range(1,len(s)): 
    a = a ^ s[i] 
if a == 0: print("NO") 
else: print("YES")