import random

N, M = map(int, input().split())

G = {}
for _ in range(M):
    v1, v2 = map(int, input().split())
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)

print(G)
def play_graph_search(graph):
    seeker_pos = random.choice(list(graph.keys()))
    hider_pos = random.choice(list(graph.keys()))
    print(seeker_pos, hider_pos)

    while seeker_pos != hider_pos:
        print(f"Seeker pos is {seeker_pos}")
        print(f"Hider pos is {hider_pos}")
        
        seeker_neighbor_pos = G[seeker_pos]
        hider_neighbor_pos = G[hider_pos]
        seeker_pos = random.choice(seeker_neighbor_pos)
        hider_pos = random.choice(hider_neighbor_pos)

    print("Seeker has found hider!")

play_graph_search(G)


