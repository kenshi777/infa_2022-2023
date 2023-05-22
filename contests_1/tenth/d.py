def count_min_cost(N, price):
    if len(price) > 1:
        C =[0, abs(price[1]-price[0])] + [0] * (N-2)
        for i in range(2, N):
            C[i] = min(abs(3*(price[i] - price[i - 2])) + C[i - 2], abs(price[i] - price[i - 1]) + C[i - 1])
        return C[N-1]
    return 0

N = int(input())
price = []
for i in range(N):
    price.append(int(input()))

print(count_min_cost(N, price))