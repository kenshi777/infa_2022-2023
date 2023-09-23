def sort_choice(arr, prev_arr):
    if len(arr) <= 1:
        return arr
    mini = min(arr)
    i_mini = arr.index(mini)
    if i_mini != 0:
        arr[0], arr[i_mini] = arr[i_mini], arr[0]
        for i in prev_arr:
            print(i, end=" ")
        for i in arr:
            print(i, end=" ")
        print("")
    arr1 = [arr[0]]
    prev_arr.append(arr[0])
    arr = arr1 + sort_choice(arr[1:], prev_arr)

    return arr


a = input().split()
for i in range(0, len(a), 1):
    a[i] = int(a[i])
sort_choice(a, [])