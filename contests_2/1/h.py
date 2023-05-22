def count_min_cost(N, height: list):
    if len(height) > 1:
        C = [0, abs(height[1] - height[0])] + [0] * (N - 2)
        for i in range(2, N):
            C[i] = min(abs(3*(height[i] - height[i - 2])) + C[i - 2], abs(height[i] - height[i - 1]) + C[i - 1])
        return C[N - 1]
    return 0

n = int(input())
height = []

for i in range(n):
    height.append(int(input()))

print(count_min_cost(n, height))