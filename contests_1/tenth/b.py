def traj_num(N, M):
    K = [1]+[0]*(N-1)
    for i in range(0, N-1):
        if i + M[i] <= N - 1:
            K[i + M[i]] += K[i]
        if M[i] != 1:
            K[i + 1] += K[i]
    return K[N-1]

N = int(input())
M = list(map(int, input().split()))

print(traj_num(N, M))