from random import randint

def Linked_list():
    return {'first' : None}
def Node(value):
    return {'value' : value, 'next' : None}
def add_to_list(value, l_list):
    new_node = Node(value)
    new_node['next'] = l_list['first']
    l_list['first'] = new_node
def pop_from_list(l_list):
    res = l_list['first']['value']
    l_list['first'] = l_list['first']['next']
    return res

def insert_value(node, value):
    new_node = Node(value)
    new_node['next'] = node['next']
    node['next'] = new_node

l = Linked_list()

for i in range(10):
    add_to_list(randint(0,100), l)

print(l)