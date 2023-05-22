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

n = int(input())
l = list(map(int, input().split()))
h = []
for i in l:
    add_to_heap(h, i)

print(*h)