arr = input().split()
l = len(arr)

def m(arr, l):
    if l > 1:
        print(*arr)
        m(arr[1:], l-1)
    else:
        print(*arr)

def f(arr, l, arr0):
    if len(arr) < len(arr0):
        m(arr, l)
        f(arr0[:l+1], l + 1, arr0)
    elif len(arr) == len(arr0):
        m(arr, l)

f(arr[:1], 1, arr)
