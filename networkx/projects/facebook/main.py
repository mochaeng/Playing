import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint

facebook = pd.read_csv(
    './facebook_combined.txt.gz',
    compression='gzip',
    sep=' ',
    names=['start_node', 'end_node']
)

GG = nx.from_pandas_edgelist(facebook, 'start_node', 'end_node')

# pos = nx.spring_layout(GG, iterations=15, seed=1721)
# fig, ax = plt.subplots(figsize=(15, 9))
# ax.axis('off')
# plot_options = {'node_size': 10, 'with_labels': False, 'width': 0.15}
# nx.draw(GG, pos=pos, ax=ax, **plot_options)
# plt.show()

print(GG.number_of_nodes())
print(GG.number_of_edges())

avg = np.mean([d for _, d in GG.degree()])
print(f'Na média um nó está conectado a: {avg} nós')

# menor caminho para entre um vértice para todos os outros
shorts_paths_lengths = dict(nx.all_pairs_shortest_path_length(GG))

print(f'Menor caminho de 1 para 42: {shorts_paths_lengths[0][42]}')

diameter = max(nx.eccentricity(GG, sp=shorts_paths_lengths).values())
print(f'Diâmetro: {diameter}')

average_path_lengths = [
    np.mean(list(spl.values())) for spl in shorts_paths_lengths.values()
]

print(f'Média do menor caminho: {np.mean(average_path_lengths)}')
