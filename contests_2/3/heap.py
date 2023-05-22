def add_to_heap(h, element):
    h.append(element)
    sift_up(h, len(h) - 1)

def sift_up(h, i):
    if i == 0:
        return
    parent_i = (i - 1) // 2

    if h[i] < h[parent_i]:
        h[i], h[parent_i] = h[parent_i], h[i]
        sift_up(h, parent_i)

def pop_from_heap(h):
    if len(h) == 0:
        raise ValueError('heap is empty')
    result = h[0]
    if len(h) == 1:
        h.pop()
        return result
    
    h[0] = h.pop()
    sift_down(h, 0)
    return result

def sift_down(h,i):
    m = min([h[i]] + h[2*i+1:2*i+3])
    if h[i] == m:
        return
    if h[2*i + 1] == m:
        h[i], h[2*i + 1] = h[2*i + 1], h[i]
        sift_down(h, 2*i+1)
    else:
        h[i], h[2*i + 2] = h[2*i + 2], h[i]
        sift_down(h, 2*i+2)

def heapify(h):
    for i in range((len(h)-1) // 2, -1, -1):
        sift_down(h, i)

# def heapify(arr, n, i):
#     largest = i
#     left = 2*i + 1
#     right = 2*i + 2
#     if left < n and arr[largest] < arr[left]:
#         largest = left
#     if right < n and arr[largest] < arr[right]:
#         largest = right
#     if largest != i:
#         arr[largest], arr[i] = arr[i], arr[largest]
#         heapify(arr, n, largest)

# def heapsort(arr):
#     n = len(arr)
#     for i in range(n,-1,-1):
#         heapify(arr,n,i)
#     for i in range(n-1,0,-1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)

a = [54, 29, 87, 78, 33, 86, 91, 54, 68, 46]
h = []
for i in a:
    add_to_heap(h, i)

heapify(a)
print(h)