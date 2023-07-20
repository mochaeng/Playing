import networkx as nx
import matplotlib.pyplot as plt

k_5 = nx.complete_graph(5)
nx.draw(k_5, with_labels=True, node_color='lightblue', node_size=3200, font_weight='bold')
plt.show()

k_3_5 = nx.complete_bipartite_graph(3, 5)
nx.draw(k_3_5, with_labels=True, node_color='lightblue', node_size=3200, font_weight='bold')
plt.show()

barbell = nx.barbell_graph(10, 10)
nx.draw(barbell, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()

lollipop = nx.lollipop_graph(10, 20)
nx.draw(barbell, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()
