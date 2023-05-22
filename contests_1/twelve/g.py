def pi_func(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        cur_len = pi[i - 1]  # длина текущего префикса
        while (cur_len > 0 and s[cur_len] != s[i]):
            cur_len = pi[cur_len - 1]
        if s[cur_len] == s[i]:
            cur_len += 1
        pi[i] = cur_len
    return pi


a = input()
b = input()
if a == b:
    print(0)
    exit(0)

#найдем,т есть ли в строке b+b строка a (если нет, то это не цикл сдвиг)
#abcdef - нач cdefab + cdefab
s = a + "#" + b + b
flag = int(0)
pi = pi_func(s)
for i in range(0, len(s)):
    if pi[i] == len(b):
        flag = 1
        print(len(a) + 2 * len(b) - i)
        exit(0)
if flag == 0:
    print(-1)
    exit(0)