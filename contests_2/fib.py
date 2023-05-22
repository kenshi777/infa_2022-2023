F = [None] * 10000
def fib(n):
    '''Фибоначи с кэшированием'''
    assert (n >= 0 and n < 10000)
    if F[n] is None:
        if n <= 1:
            F[n] = n
        else:
            F[n] = fib(n-1) + fib(n-2)
    return F[n]

print(fib(20))