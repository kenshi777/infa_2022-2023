def rabin_karp(text, pattern):
    # определяем длину текста и шаблона
    n = len(text)
    m = len(pattern)
    l = []
    # определяем простое число p для вычисления хэша
    p = 31
    # вычисляем p в степени m-1
    power = 1
    for i in range(m-1):
        power = (power * p) % 1000000007
    # вычисляем хэш для шаблона и первой подстроки текста
    pattern_hash = 0
    text_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % 1000000007
        text_hash = (text_hash * p + ord(text[i])) % 1000000007
    # проходим по всем подстрокам текста
    for i in range(n-m+1):
        # если хэши равны, проверяем подстроку на совпадение со шаблоном
        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                l.append(i)
        # вычисляем хэш для следующей подстроки текста
        if i < n-m:
            text_hash = (text_hash - ord(text[i]) * power) % 1000000007
            text_hash = (text_hash * p + ord(text[i+m])) % 1000000007
    return " ".join(map(str, l)) if l != [] else -1
pattern = input()
text = input()
print(rabin_karp(text, pattern))