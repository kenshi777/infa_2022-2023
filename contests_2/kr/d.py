def heapify(arr, n, i):
    largest = i 
    left = 2 * i + 1   
    right = 2 * i + 2   

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapsort(A):
    n = len(A)

    for i in range(n, -1, -1):
        heapify(A, n, i)
    print(*A)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
        print(*A)