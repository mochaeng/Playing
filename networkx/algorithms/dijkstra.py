import networkx as nx
import matplotlib.pyplot as plt

edges = [
    (1, 2, {"weight": 4}),
    (1, 3, {"weight": 1}),
    (1, 5, {"weight": 2}),
    (2, 3, {"weight": 1}),
    (2, 4, {"weight": 5}),
    (3, 4, {"weight": 8}),
    (3, 5, {"weight": 10}),
    (4, 5, {"weight": 2}),
    (4, 6, {"weight": 8}),
    (5, 6, {"weight": 5}),
    (4, 9, {"weight": 5}),
    (10, 3, {"weight": 3}),
]

g = nx.from_edgelist(edges)

shortest_path_lengths = list(nx.all_shortest_paths(g, source=1, target=2, weight='weight'))
print(shortest_path_lengths)

all_shortest_path_lengths = dict(nx.shortest_path_length(g, weight='weight'))
print(all_shortest_path_lengths)
print(all_shortest_path_lengths[1][2])


# Drawing
pos = nx.planar_layout(g)
plot_options = {'node_size': 800, 'with_labels': True, 'width': 1.15, 'font_weight': 'bold'}
nx.draw(g, pos, **plot_options)
nx.draw_networkx_edges(g, pos, edgelist=edges, width=1.15)
nx.draw_networkx_labels(g, pos, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(g, "weight")
nx.draw_networkx_edge_labels(g, pos, edge_labels)
plt.show()
