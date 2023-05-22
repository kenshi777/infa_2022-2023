from queue import Queue
from random import randint
import heapq

N, M = map(int, input().split())

G = {}
for _ in range(M):
    v1, v2 = input().split()
    for v in (v1, v2):
        if v not in G:
            G[v] = {}
    G[v1][v2] = G[v2][v1] = randint(10,99)

def deikstra_1(G, start):
    distances = {v: float('+inf') for v in G}

    q = Queue()
    q.put(start)
    distances[start] = 0

    while not q.empty():
        v = q.get()
        for neighbour in G[v]:
            tmp = distances[v] + G[v][neighbour]
            if distances[neighbour] > tmp:
                q.put(neighbour)
                distances[neighbour] = tmp
    return distances

def deikstra_2(G, start):
    heap = []
    distances = {v: float('+inf') for v in G}
    distances[start] = 0
    heapq.heappush(heap, (0, start))

    while len(heap) > 0:
        v = heapq.heappop(heap)[1]
        for neighbour in G[v]:
            tmp = distances[v] + G[v][neighbour]
            if distances[neighbour] > tmp:
                heapq.heappush(heap, (tmp, neighbour))
                distances[neighbour] = tmp
    return distances

print(G)
print(deikstra_1(G, 'A'))
print(deikstra_2(G, 'A'))