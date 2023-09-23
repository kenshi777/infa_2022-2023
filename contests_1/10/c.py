def count_trajectories(N, cell: list, paint: list):
    k = [0, 1] + [0] * (N - 1)
    for i in range(1, N):
        if cell[i] == cell[i - 1] or cell[i] == paint[i - 1]:
            k[i + 1] += k[i]
        if cell[i] == cell[i - 2] or cell[i] == paint[i - 2]:
            k[i + 1] += k[i - 1]
    return k[N]

N = int(input())
cell = list(map(int, input().split()))
paint = list(map(int, input().split()))

print(count_trajectories(N, cell, paint) % 947)