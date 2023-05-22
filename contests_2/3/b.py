l = input().split()
stack = []
error = False
if len(l) == 0:
    error = True
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

for i in range(len(l)):
    if is_number(l[i]):
        stack.append(float(l[i]))
    elif i == 0:
        error = True
        break
    elif l[i] == '#':
        s = sum(stack)
        stack = [s]
    elif l[i] == '%' and i == 1:
        error = True
        break
    else:
        s = (stack[0] / 100) * stack[1]
        stack = [s]

if len(stack) == 0:
    error = True

print(0.0 if error else stack[-1])





