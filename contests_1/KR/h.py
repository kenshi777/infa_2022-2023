def cycle_shift_M(arr, N, M):
    for i in range(M % N):
        arr.append(arr[0])
        arr.pop(0)

    return arr


print(cycle_shift_M([1, 2, 3, 4, 5], 5, 2))