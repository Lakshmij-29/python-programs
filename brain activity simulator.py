import networkx as nx
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(15, 0.3)

nx.draw(G, with_labels=True)
plt.title("Neural Network Simulation")
plt.show()
