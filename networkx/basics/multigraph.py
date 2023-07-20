import networkx as nx
import matplotlib.pyplot as plt

# Multigraph: permite várias arestas entre quaisquer vertices

MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.15)])
print(dict(MG.degree(weight='weight')))

GG = nx.Graph()
for edge_from, edge_from_adj in MG.adj.items():
    for edge_to, edict in edge_from_adj.items():
        # aresta com menor valor
        min_value = min([d['weight'] for d in edict.values()])
        GG.add_edge(edge_from, edge_to, weight=min_value)

print(nx.shortest_path(GG, 1, 3))

pos = nx.planar_layout(MG)
nx.draw(MG, pos, with_labels=True, node_color='lightblue', node_size=3200, font_weight='bold')
plt.show()
