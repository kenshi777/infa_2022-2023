def is_correct(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    return not s

print('YES' if is_correct(input()) else 'NO')