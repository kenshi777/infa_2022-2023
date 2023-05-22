def BinTree():
    return {'root' : None}

def Node(value):
    return {'left' : None,
            'right' : None,
            'value' : value}

def insert_to_tree(t, value):
    if t['root'] is None:
        t['root'] = Node(value)
    else:
        insert_to_node(t['root'], value)

def insert_to_node(node, value):
    if value == node['value']:
        return
    if value > node['value']:
        if node['right'] is None:
            node['right'] = Node(value)
        else:
            insert_to_node(node['right'], value)
    else:
        if node['left'] is None:
            node['left'] = Node(value)
        else:
            insert_to_node(node['left'], value)
def height(node):
    # Если узел пустой, то высота равна 0
    if node is None:
        return 0
    # Рекурсивно находим высоту левого и правого поддеревьев
    left_height = height(node['left'])
    right_height = height(node['right'])
    # Высота дерева равна максимальной из высот левого и правого поддеревьев, плюс 1 (за учетом узла)
    return max(left_height, right_height) + 1


t = BinTree()

l = list(map(int, input().split()))

for i in l:
    insert_to_tree(t, i)

print(height(t['root']))