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
