import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
D = nx.DiGraph()
D.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4), (4, 2)])
# Create an undirected graph
U = nx.Graph()
U.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4), (4, 2)])
# Visualize both graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
nx.draw(D, with_labels=True, node_color='lightgreen',
 node_size=500, font_weight='bold', ax=ax1,
 arrows=True)
ax1.set_title("Directed Graph")
nx.draw(U, with_labels=True, node_color='lightblue',
 node_size=500, font_weight='bold', ax=ax2)
ax2.set_title("Undirected Graph")
plt.tight_layout()
plt.show()
