def is_bst(arr, index, minimum = float('-inf'), maximum = float('+inf')):
    if index == -1:
        return True
    elif maximum < arr[index][0] or arr[index][0] < minimum:
        return False
    else:
        return is_bst(arr, arr[index][1], minimum, arr[index][0]) and is_bst(arr, arr[index][2], arr[index][0], maximum)
    
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print('YES' if is_bst(arr, 0 ) else 'NO')