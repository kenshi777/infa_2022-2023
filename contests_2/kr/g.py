numbers = list(map(int, input().split()))

stack = list()

for i in range(len(numbers) - 1):
    number = numbers[i]
    if number > 0:
        stack.append(number)
    elif len(stack) > 0 and number < 0 and abs(number) < stack[len(stack) - 1]:
        stack[len(stack) - 1] += number
    elif len(stack) > 0 and number < 0 and abs(number) >= stack[len(stack) - 1]:
        stack.pop(len(stack) - 1)


print(len(stack), end=' ')

if len(stack) == 0:
    print(-1)
else:
    print(stack[len(stack) - 1])