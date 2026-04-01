import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
connections = [('Alice','Bob'), ('Alice','Charlie'), ('Bob','David'), ('Charlie','David'), ('David','Eve')]

G.add_edges_from(connections)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, edge_color='gray')
plt.show()
