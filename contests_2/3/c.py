stack = []
n = 0

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    
while n != '=':
    n = input()
    if is_number(n):
        stack.append(int(n))
    elif n == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)
    elif n == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)
    elif n == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a*b)

print(*stack)