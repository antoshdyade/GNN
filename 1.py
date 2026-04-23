import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()
# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5])
# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])
# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue',
 node_size=500, font_weight='bold')
plt.title("Simple Undirected Graph")
plt.show()
