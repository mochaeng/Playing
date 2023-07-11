# Fila de Prioridade Máxima

A _Priority Queue_ pode ser feita por meio de _array_, _lista encadeada_ ou _árvore binária_, entranto a melhor solução é feita com um _Heap_.

O _heap_ é uma árvore binária em que cada nó satisfaz:

> Para cada nó, o seu valor é maior ou igual a valor dos seus filhos.

O código está no arquivo: [_MaxPriorityQueue.py_](MaxPriorityQueue.py)

Há também um examplo: [_PacketsExample_](PacketsExample.py). Com o que deveria ser pacotes

```python
class Packet:
    def __init__(self, priority: int):
        self.id = uuid4()
        self.header = 'Version | Flags | Protocol | TTL'
        self.priority = priority

    def __ge__(self, other):
        return self.priority >= other.priority


packets = [Packet(15), Packet(12), Packet(1), Packet(26), Packet(24),
           Packet(35), Packet(2), Packet(5), Packet(33), Packet(34), Packet(4)]

pq = PriorityQueue()

for packet in packets:
    pq.push(packet)

print(pq) # {35,34,26,24,33,1,2,5,12,15,4}
```

```python
for packet in packets:
    top = pq.pop()
    print(top.priority)

    # 35
    # 34
    # 33
    # 26
    # 24
    # 15
    # 12
    # 5
    # 4
    # 2
    # 1
```
