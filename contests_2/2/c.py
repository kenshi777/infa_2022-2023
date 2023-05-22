def polynom_hash(base, module, s):
    polynom = 0
    for i in range(len(s)):
        polynom += ord(s[i]) * base ** (len(s)-i-1)
    hash = polynom % module
    return hash


def search(table, key):
    hash_val = polynom_hash(91, 100, key) % 10
    for chain in table[hash_val]:
        if chain[1] == key:
            return chain[2]
    return 'KeyError'
            
example_table = [
    [], [],
    [
        [32, 'ONLY', 'alsdmakl'],
        [62, 'INDUSTRY', 'lfow'],
        [72, 'LETRASET', 'awdwad'],
        [32, 'BEEN', 'lkawdk']
    ],
    [], [], [], [], [], [], [],
]
v1 = search(example_table, 'ONLY')      # v1 == 'lkawdk'
v2 = search(example_table, 'PRODUCT')   # v2 == 'KeyError'
# print(polynom_hash(91, 100, 'None'))

print(v1)
print(v2)
# print(example_table[2][0][2] is not None)