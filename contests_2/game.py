import networkx as nx
import random

def play_graph_search(graph):
    seeker_position = random.choice(list(graph.nodes()))
    hider_position = random.choice(list(graph.nodes()))
    
    while seeker_position != hider_position:
        print(f"Seeker is at node {seeker_position}")
        print(f"Hider is at node {hider_position}")
        
        neighbor_nodes = list(graph.neighbors(seeker_position))
        next_node = random.choice(neighbor_nodes)
        seeker_position = next_node
        
    print("Seeker has found the hider!")

# Создаем граф
graph = nx.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Запускаем игру
play_graph_search(graph)
