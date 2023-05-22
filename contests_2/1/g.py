K, M = int(input()), int(input())

def unjumania(K, M, sum, number):
    if M == 1:
        sum += K + number
        print(sum)
    else:
        sum += (K + number)*2
        unjumania(K, M-1, sum, number + 1)

unjumania(K, M, 0, 0)