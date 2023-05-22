def make_exchange(money, coins):
    if money == 0:
        return 1
    if money < 0:
        return 0
    if len(coins) == 0:
        return 0
    coins1 = coins
    coins1 = coins[1:]
    return make_exchange(money, coins1) + make_exchange(money - coins[0], coins)