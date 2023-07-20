import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # undirected graph

# adding nodes
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {'color': 'red'}),
    (5, {'color': 'green'}),
])  # node attributes

G.add_edge(1, 2)
G.add_edges_from([(2, 2), (1, 3)])


# pos = nx.planar_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3200, font_weight='bold')
# plt.show()


FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for edge_from, edge_from_adj in FG.adj.items():
    for edge_to, edge_attr in edge_from_adj.items():
        wt = edge_attr['weight']
        if wt < 0.5:
            print(f'({edge_from}, {edge_to}, {wt:.3})')

print()

# sem percorrer duas vezes
for (u, v, wt) in FG.edges.data('weight'):
    if wt < 0.5:
        print(f'({u}, {v}, {wt:.3})')

# pos = nx.planar_layout(FG)
# nx.draw(FG, pos, with_labels=True, node_color='lightblue', node_size=3200, font_weight='bold')
# plt.show()

# edges, nodes e graphs podem guardar atributos
G = nx.Graph()
G.add_edge(1, 2, weight=1.3)  # weight atributo (numerico) especial
G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': '8'})])

print(G[1][2])
G[1][2]['weight'] = 9
print(G[1][2])

G.edges[3, 4]['weight'] = 4  # cria-se 'weight'
print(G.edges[3, 4])

G.nodes[1]['time'] = '5pm'
print(G.nodes[1])

print(list(G.neighbors(2)))

pos = nx.planar_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3200, font_weight='bold')
plt.show()
