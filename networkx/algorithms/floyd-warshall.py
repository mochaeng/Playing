import networkx as nx
import matplotlib.pyplot as plt

edges = [(1, 2, {'weight': 4}),
         (1, 3, {'weight': 2}),
         (2, 3, {'weight': 1}),
         (2, 4, {'weight': 5}),
         (3, 4, {'weight': 8}),
         (3, 5, {'weight': 10}),
         (4, 5, {'weight': 2}),
         (4, 6, {'weight': 8}),
         (5, 6, {'weight': 5})]

g = nx.Graph()
g.add_edges_from(edges)

fw = dict(nx.floyd_warshall(g, weight='weight'))
for u, v in fw.items():
    print(u, dict(v))


# Drawing
pos = nx.planar_layout(g)
plot_options = {'node_size': 800, 'with_labels': True, 'width': 1.15, 'font_weight': 'bold'}
nx.draw(g, pos, **plot_options)
# draw edges labels
nx.draw_networkx_edges(g, pos, edgelist=edges, width=1.15)
nx.draw_networkx_labels(g, pos, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(g, "weight")
nx.draw_networkx_edge_labels(g, pos, edge_labels)
plt.show()
