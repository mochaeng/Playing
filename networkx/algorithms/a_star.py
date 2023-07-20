import networkx as nx
import matplotlib.pyplot as plt


def euclidian(a, b):
    (x1, y1) = a
    (x2, y2) = b

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


g = nx.grid_graph(dim=[3, 3])
edge_list = {e: e[1][0] * 2 for e in g.edges()}

print(edge_list)

nx.set_edge_attributes(g, edge_list, 'cost')

path = nx.astar_path(g, (0, 0), (2, 2), heuristic=euclidian, weight='cost')
length = nx.astar_path_length(g, (0, 0), (2, 2), heuristic=euclidian, weight='cost')
print(f'Path: {path}')
print(f'Path length: {length}')


# Drawing
pos = nx.planar_layout(g)
plot_options = {'node_size': 1600, 'with_labels': True, 'node_color': 'orange'}
nx.draw(g, pos, **plot_options)
# draw edges labels
nx.draw_networkx_labels(g, pos)
edge_labels = nx.get_edge_attributes(g, "cost")
nx.draw_networkx_edge_labels(g, pos, edge_labels)
plt.show()
