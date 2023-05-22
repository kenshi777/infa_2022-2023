def is_add_35(n):
    m = n - 1
    if m % 5 == 0:
        return True
    elif m < 0:
        return False
    else:
        return is_add_35(n-3)