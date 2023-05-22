s = input().split()

def count_sum_ord(s1: str):
    n = 0
    for i in range(len(s1)):
        n += ord(s1[i])
    return n

for i in s:
    if len(i) >= 5:
        print(count_sum_ord(i), end=' ')