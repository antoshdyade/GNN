import networkx as nx
import matplotlib.pyplot as plt

# Create a simple citation network
citations = nx.DiGraph()

# Add papers as nodes with attributes
papers = {
    'Paper1': {'title': 'GNN Fundamentals', 'year': 2017, 'citations': 420},
    'Paper2': {'title': 'Graph Convolutional Networks', 'year': 2016, 'citations': 830},
    'Paper3': {'title': 'GraphSAGE', 'year': 2017, 'citations': 620},
    'Paper4': {'title': 'Graph Attention Networks', 'year': 2018, 'citations': 590},
    'Paper5': {'title': 'Graph Neural Networks Review', 'year': 2019, 'citations': 380},
    'Paper6': {'title': 'GNN Applications', 'year': 2020, 'citations': 210},
    'Paper7': {'title': 'Advanced GNN Methods', 'year': 2021, 'citations': 150}
}

# Add nodes
for paper_id, attributes in papers.items():
    citations.add_node(paper_id, **attributes)

# Add citation edges
citation_edges = [
    ('Paper3', 'Paper2'),
    ('Paper4', 'Paper2'), ('Paper4', 'Paper3'),
    ('Paper5', 'Paper1'), ('Paper5', 'Paper2'),
    ('Paper5', 'Paper3'), ('Paper5', 'Paper4'),
    ('Paper6', 'Paper1'), ('Paper6', 'Paper5'),
    ('Paper7', 'Paper4'), ('Paper7', 'Paper5'),
    ('Paper7', 'Paper6')
]
citations.add_edges_from(citation_edges)

# Analyze in-degree
in_degree = dict(citations.in_degree())
print("Times Cited Within Network:")
for paper, times_cited in sorted(in_degree.items(), key=lambda x: x[1], reverse=True):
    print(f"{papers[paper]['title']}: {times_cited}")

# --- Visualization ---
fig, ax = plt.subplots(figsize=(12, 8))

pos = nx.spring_layout(citations, seed=42)

node_colors = [papers[node]['year'] - 2015 for node in citations.nodes()]
node_sizes = [papers[node]['citations'] / 10 for node in citations.nodes()]

# Draw nodes separately (important for colorbar)
nodes = nx.draw_networkx_nodes(
    citations,
    pos,
    node_color=node_colors,
    cmap=plt.cm.viridis,
    node_size=node_sizes,
    ax=ax
)

# Draw edges
nx.draw_networkx_edges(citations, pos, ax=ax, arrows=True)

# Draw labels
label_pos = {k: (v[0], v[1] + 0.02) for k, v in pos.items()}
labels = {node: papers[node]['title'] for node in citations.nodes()}
nx.draw_networkx_labels(citations, label_pos, labels=labels, font_size=8, ax=ax)

# Title
ax.set_title("Citation Network (node size: citation count, color: publication year)")

# Add colorbar (correct way)
cbar = plt.colorbar(nodes, ax=ax)
cbar.set_label('Years since 2015')

plt.show()
