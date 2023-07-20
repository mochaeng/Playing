import networkx as nx
import matplotlib.pyplot as plt

with open('./graph.txt') as f:
    lines = f.readlines()

edges = [line.strip().split() for line in lines]

g = nx.Graph()
g.add_edges_from(edges)

dfs = nx.dfs_tree(g, source='go')

# Drawing
pos = nx.planar_layout(g)
plot_options = {'node_size': 800, 'with_labels': True, 'width': 1.15, 'font_weight': 'bold'}
nx.draw(g, pos, **plot_options)
nx.draw(dfs, pos, edge_color='#dd2222', **plot_options)
plt.show()
