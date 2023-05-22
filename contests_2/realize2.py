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

def play_territory_capt(graph):
    nodes = list(set(graph.keys()))
    player1_terr = set()
    player2_terr = set()
    
    while len(player1_terr) + len(player2_terr) < len(nodes):
        print(f"Player 1 territory: {player1_terr}")
        print(f"Player 2 territory: {player2_terr}")
        player1_pos = G[random.choice(player1_terr)]
        player2_pos = G[random.choice(player1_terr)]
        available_nodes_1 = set(graph.keys()) - player1_terr - player2_terr
        available_nodes_2 = set(graph.keys()) - player1_terr - player2_terr
        selected_node = random.choice(list(available_nodes))

        if len(player1_terr) <= len(player2_terr):
                player1_terr.add(selected_node)
        else:
            player2_terr.add(selected_node)

    print("Game over!")
    print(f"Player 1 territory: {player1_terr}")
    print(f"Player 2 territory: {player2_terr}")

play_territory_capt(G)