def fix(n, start, finish, HANOI_PATH):
    if n > 0:
        if (start + finish) == 4:
            fix(n, start, 2, HANOI_PATH)
            fix(n, 2, finish, HANOI_PATH)
        else:
            fix(n - 1, start, 6 - start - finish, HANOI_PATH)
            HANOI_PATH.append([n, start, finish])
            fix(n - 1, 6 - start - finish, finish, HANOI_PATH)


HANOI_PATH = list()
fix(N, 1, 3, HANOI_PATH)
