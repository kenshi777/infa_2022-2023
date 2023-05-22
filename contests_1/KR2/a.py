l = input().split()
l_sorted = sorted(l, key=len)
print(len(l_sorted[0]), len(l_sorted[-1]))
