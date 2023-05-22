def polynom_hash(base, module, s):
    polynom = 0
    for i in range(len(s)):
        polynom += ord(s[i]) * base ** (len(s)-i-1)
    hash = polynom % module
    return hash

def remove(table, key):
    hash_val = polynom_hash(91, 100, key) % 10
    for i in range(len(table[hash_val])):
        if table[hash_val][i][1] == key:
            k = table[hash_val][i][2]
            table[hash_val].pop(i)
            return k
    return 'KeyError'

# исходное состояние таблицы
example_table = [
    [], [],
    [
        [32, 'ONLY', 'pal;cw'],
        [62, 'INDUSTRY', 'lfow'],
        [72, 'LETRASET', 'awdwad'],
        [32, 'BEEN', 'lkawdk'],
    ],
    [], [], [], [], [], [], [],
]
v1 = remove(example_table, 'BEEN')      # v1 == 'lkawdk'
v2 = remove(example_table, 'PRODUCT')   # v2 == 'KeyError'
# таблица принимает вид (элемент с ключом 'BEEN' удалён)
# example_table = [
#     [], [],
#     [
#         [32, 'ONLY', 'pal;cw'],
#         [62, 'INDUSTRY', 'lfow'],
#         [72, 'LETRASET', 'awdwad'],
#     ],
#     [], [], [], [], [], [], [],
# ]

print(v1)
print(v2)
print(example_table)