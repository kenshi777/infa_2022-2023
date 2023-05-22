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
def find_leaf(node, leaves):
    if node['right'] is None and node['left'] is None:
        leaves.append(node['value'])
    if node['right'] is not None:
        find_leaf(node['right'], leaves)
    if node['left'] is not None:
        find_leaf(node['left'], leaves)

t = BinTree()

l = list(map(int, input().split()))

for i in l:
    insert_to_tree(t, i)

leaves = []
find_leaf(t['root'], leaves)
print(*sorted(leaves))