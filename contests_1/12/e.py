b = input() #подстрока
a = input() #строка
s = b + "#" + a #решетки точно нет в a и b => останется найти те значения префикс функции, которые равны len(b)

#считаем префикс функцию
pi = [0] * len(s)
for i in range(1, len(s)):
    cur_len = pi[i - 1] #длина текущего префикса
    while(cur_len > 0 and s[cur_len] != s[i]):
        cur_len = pi[cur_len - 1]
    if s[cur_len] == s[i]:
        cur_len += 1
    pi[i] = cur_len

flag = int(0)
for i in range(0, len(s)):
    if pi[i] == len(b):
        flag = 1
        print(i - len(b) - 1 + 1 - len(b))  #bbbb # aaaaaa

if flag == 0:
    print(-1)