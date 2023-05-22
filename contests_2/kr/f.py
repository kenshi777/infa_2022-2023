amount = int(input())

stack = []
for i in range(amount):
    comm = input()
    if comm[2:].isdigit() and comm[0] == '+':
        stack.append(int(comm[2:]))
    elif comm[2:].isdigit() and comm[0] == '*':
        stack.insert(len(stack) // 2 + len(stack) % 2, int(comm[2:]))
    elif comm == '-':
        print(stack.pop(0))