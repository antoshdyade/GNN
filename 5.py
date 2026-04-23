import networkx as nx
import matplotlib.pyplot as plt

# Create a social network graph
social = nx.Graph()
social.add_edges_from([
 ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice',
'David'),
 ('Bob', 'Charlie'), ('David', 'Eve'), ('Eve', 'Frank'),
 ('David', 'Frank'), ('Charlie', 'George')
])
# Calculate degree centrality
degree_cent = nx.degree_centrality(social)
print("Degree Centrality:")
for node, centrality in sorted(degree_cent.items(),
 key=lambda x: x[1],
reverse=True):
 print(f"{node}: {centrality:.3f}")

# Calculate betweenness centrality
betweenness_cent = nx.betweenness_centrality(social)
print("\nBetweenness Centrality:")
for node, centrality in sorted(betweenness_cent.items(),
 key=lambda x: x[1],
reverse=True):
 print(f"{node}: {centrality:.3f}")

# Calculate clustering coefficient
clustering = nx.clustering(social)
print("\nClustering Coefficient:")
for node, coef in sorted(clustering.items(),
 key=lambda x: x[1], reverse=True):
 print(f"{node}: {coef:.3f}")

# Visualize the social network with size proportional to degree centrality
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(social, seed=42)
node_size = [degree_cent[node] * 3000 for node in social]
nx.draw(social, pos, with_labels=True, node_color='lightblue',
 node_size=node_size, font_weight='bold')
plt.title("Social Network (node size proportional to degree centrality)")
plt.show()

