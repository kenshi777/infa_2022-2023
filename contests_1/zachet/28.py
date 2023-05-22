def generate_numbers(N, M, prefix = None):
    if M == 0:
        print(*prefix)
    else:
        prefix = prefix or []
        for i in range(N):
            prefix.append(i)
            generate_numbers(N, M-1, prefix)
            prefix.pop()

generate_numbers(3, 3)
