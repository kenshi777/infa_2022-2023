N = int(input())
L = []
nums = [_ for _ in range(1,100)]
counts = [0] * 99
for i in range(N):
    L.append(int(input()))

for i in range(N):
    for j in range(len(nums)):
        if L[i] == nums[j]:
            counts[j]+= 1

max_num = counts[0]
for i in range(len(counts)):
    if max_num < counts[i]:
        max_num = counts[i]

print(counts.index(max_num)+1)

