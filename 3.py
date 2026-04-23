import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted graph
W = nx.Graph()
# Add edges with weights
weighted_edges = [(1, 2, 0.5), (2, 3, 1.2), (1, 3, 0.8),
 (3, 4, 2.1), (4, 2, 0.9)]
W.add_weighted_edges_from(weighted_edges)
# Get edge weights for labeling
edge_labels = {(u, v): f"{w:.1f}" for u, v, w in
weighted_edges}

#Visualize the weighted graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(W, seed=42) #Layout for consistent positioning


nx.draw(W, pos, with_labels=True, node_color='lightsalmon',
node_size=500, font_weight='bold')
nx.draw_networkx_edge_labels(W, pos, edge_labels=edge_labels)
plt.title("Weighted Graph")
plt.show()
