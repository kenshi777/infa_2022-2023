import networkx as nx
import matplotlib.pyplot as plt

def play_territory_capture(graph):
    player1_territory = set()
    player2_territory = set()
    
    while len(player1_territory) + len(player2_territory) < len(graph.nodes()):
        print(f"Player 1 territory: {player1_territory}")
        print(f"Player 2 territory: {player2_territory}")
        
        available_nodes = set(graph.nodes()) - player1_territory - player2_territory
        selected_node = int(input("Select a node to capture: "))
        
        if selected_node in available_nodes:
            if len(player1_territory) <= len(player2_territory):
                player1_territory.add(selected_node)
            else:
                player2_territory.add(selected_node)
        else:
            print("Invalid move. Try again.")
    
    print("Game over!")
    print(f"Player 1 territory: {player1_territory}")
    print(f"Player 2 territory: {player2_territory}")

# Создаем граф
graph = nx.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Рисуем граф
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue')
plt.show()

# Запускаем игру
play_territory_capture(graph)
