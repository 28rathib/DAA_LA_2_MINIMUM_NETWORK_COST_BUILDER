import networkx as nx
import matplotlib.pyplot as plt

# Union-Find Data Structure (Disjoint Set Union)
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            self.parent[root2] = root1


# Kruskal's Algorithm for Minimum Spanning Tree (MST)
def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(vertices)
    mst = []          
    total_cost = 0

    for u, v, cost in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, cost))
            total_cost += cost

    return mst, total_cost

# Visualization of the Network
def visualize_network(mst_edges, total_cost):
    G = nx.Graph()

    for u, v, cost in mst_edges:
        G.add_edge(u, v, weight=cost)

    pos = nx.spring_layout(G, seed=42)  

    nx.draw(G, pos, with_labels=True, node_color='lightgreen',
            node_size=1500, font_size=12, font_weight='bold', edge_color='gray')

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='blue')

    plt.title(f" Minimum Cost Power Substation Network\nTotal Cost = {total_cost}")
    plt.show()


# Main Program
if __name__ == "__main__":
    print("=== Minimum Cost Network Builder ===")
    print("Example: Power Companies Connecting Substations\n")

    vertices = ['A', 'B', 'C', 'D']
    edges = [
        ('A', 'B', 10),
        ('A', 'C', 6),
        ('B', 'C', 5),
        ('B', 'D', 15),
        ('C', 'D', 4)
    ]

    mst_edges, total_cost = kruskal(vertices, edges)

    print("Edges Included in the Minimum Cost Network:")
    for u, v, cost in mst_edges:
        print(f"{u} -- {v}   (Cost: {cost})")
    print("\nTotal Minimum Cost =", total_cost)

    visualize_network(mst_edges, total_cost)

