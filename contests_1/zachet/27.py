def hanoi(n, i = 1, j = 3):
    if n == 1:
        print(i, j)
        return
    else:
        hanoi(n-1, i, 6-i-j)
        print(i, j)
        hanoi(n-1, 6-i-j, j)

hanoi(5)
