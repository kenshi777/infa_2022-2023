stack, variables, commands = [], {}, input().split()

if commands[-1] != '=':
    print('incorrect')
    exit(0)

for el in commands:
    if el not in ['+', '-', '*', '/', '='] and not el.isdigit():
        variables[el] = 0
for i in range(len(variables)):
    var = input().split()
    if var[0] in variables.keys():
        variables[var[0]] = var[1]
    else:
        print('incorrect')
        exit(0)        

for comm in commands:
    if comm.isdigit():  
        stack.append(int(comm))
    elif comm in variables.keys():
        stack.append(int(variables[comm]))
    elif comm == '+':  
        if len(stack) >= 2:
            stack[-2] += stack[-1]
            del stack[-1] 
        else:
            print('incorrect')
            exit(0)
    elif comm == '-': 
        if len(stack) >= 2:
            stack[-2] -= stack[-1]
            del stack[-1]  
        else:
            print('incorrect')
            exit(0)
    elif comm == '*':
        if len(stack) >= 2:
            stack[-2] *= stack[-1]
            del stack[-1] 
        else:
            print('incorrect')
            exit(0)
    elif comm == '/': 
        if len(stack) >= 2:
            stack[-2] //= stack[-1]
            del stack[-1]  
        else:
            print('incorrect')
            exit(0)
    
if len(stack) == 1:
    print(stack[0])
else:
    print('incorrect')