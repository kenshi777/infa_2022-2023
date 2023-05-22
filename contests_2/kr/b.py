from collections import deque

sequence = list(map(int, input().split()))

hierarchy = list(map(int, input().split()))

for i in range(len(sequence)):
    print(*hierarchy[:hierarchy.index(sequence[i]) + 1], end=' ')