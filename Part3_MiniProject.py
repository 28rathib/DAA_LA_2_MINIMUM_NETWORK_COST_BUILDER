# ---- Visualization of Minimum Cost Network ----
import networkx as nx
import matplotlib.pyplot as plt

# Edges from the Kruskal’s MST example
edges = [
    ('C', 'D', 4),
    ('B', 'C', 5),
    ('A', 'C', 6)
]

G = nx.Graph()

for u, v, cost in edges:
    G.add_edge(u, v, weight=cost)

pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1200, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Minimum Cost Network (Power Substations)")
plt.show()
