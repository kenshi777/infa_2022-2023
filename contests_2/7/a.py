from queue import Queue

n, m = list(map(int, input().split()))

def read_graph(M):
    G = dict()
    for i in range(M):
        v1, v2 = list(map(int, input().split()))
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        G[v2].append(v1)
    return G

def cycle(G, start, m, n):
    parent = {v: None for v in G}

    q = Queue()
    q.put(start)
    parent[start] = None  # ищем путь от стартовй першины, до остальных

    while not q.empty():
        v = q.get()
        for neighbor in G[v]:
            if parent[neighbor] is None:
                q.put(neighbor)
                parent[neighbor] = v #создаем список откуда мы пришлм
            elif parent[neighbor] != v:
                # print(parent)
                if m == n - 1:
                    pass
                elif v in G[parent[neighbor]] and parent[neighbor] in G[v]:
                    # print(parent[neighbor], v)
                    G[parent[neighbor]].remove(v)
                    G[v].remove(parent[neighbor])
                    # parent[v] = None
                    m -= 1
                    #print(parent)

                    #print(G)

    return G

graph = read_graph(m)

#print(graph)

new_graph = cycle(graph, list(graph.keys())[0], m, n)

for key in new_graph.keys():
    for v in new_graph[key]:
        print(key, v)
        new_graph[v].remove(key)