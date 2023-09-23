s = input().split()

s_sorted = sorted(s)
s_sorted_len = sorted(s_sorted, key=len)


def count_sum_ord(s1: str):
    sum_ord = 0
    for i in range(len(s1)):
        sum_ord += ord(s1[i])
    return sum_ord

for i in s_sorted_len:
    print(count_sum_ord(i), end=' ')