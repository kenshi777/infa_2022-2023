cash = [1, 1] + [0]*100
def fibonacci(N):
    if N <= 1:
        return 1
    if cash[N-1] == 0:
        cash[N-1] = fibonacci(N-1)
    if cash[N-2] == 0:
        cash[N-2] = fibonacci(N-2)
    return cash[N-1] + cash[N-2]

N = int(input())
print(fibonacci(N))