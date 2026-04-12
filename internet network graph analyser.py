import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("Router", "Laptop"),
    ("Router", "Mobile"),
    ("Router", "Server"),
    ("Server", "Database")
])

nx.draw(G, with_labels=True, node_size=2000)
plt.show()
