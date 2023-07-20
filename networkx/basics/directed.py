import networkx as nx
import matplotlib.pyplot as plt

# directed graph
H = nx.DiGraph()
H.add_edge(2, 1)
H.add_edge(1, 3)
H.add_edge(2, 4)
H.add_edge(1, 2)

pos = nx.planar_layout(H)
nx.draw(H, pos, with_labels=True, node_color='lightblue', node_size=3200, font_weight='bold')
plt.show()

DG = nx.DiGraph()

DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75), (2, 3, 1.0)])

print(DG.edges[1, 2])

