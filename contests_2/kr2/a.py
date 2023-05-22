amount = int(input())
bag = dict()

for i in range(amount):
    word = input().lower()
    if word in bag.keys():
        bag[word] += 1
    else:
        bag[word] = 1
        
bag = {k: bag[k] for k in sorted(bag, key=bag.get, reverse=True)}

max_value = max(bag.values())  # maximum value
max_keys = [k for k, v in bag.items() if v == max_value]

print(max_keys[0], max_value)