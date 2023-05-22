def cycle_shift(arr, N):
    if N == 1:
        return arr
    else:
        arr[0], arr[N-1] = arr[N-1], arr[0]
        for i in range(N-2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
