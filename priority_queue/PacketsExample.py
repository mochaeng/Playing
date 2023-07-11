from MaxPriorityQueue import PriorityQueue

from uuid import uuid4


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

print(pq)

for packet in packets:
    top = pq.pop()
    print(top.priority)

print(pq)
