# article https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/

# idx * 2     (left child)
# idx * 2 + 1 (right child)
# idx / 2     (parent)

class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.arr_to_heap()

    def size(self) -> int:
        return len(self.arr) - 1

    def arr_to_heap(self):
        for i in range(int(self.size() / 2), 0, -1):
            self.max_heapify(i)

    def extract_maximum(self) -> int:
        maximum = self.maximum()
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        self.max_heapify(1)  # reorganize the heap
        return maximum

    def insert_value(self, value):
        self.arr.append(value)
        idx: int = int(self.size())

        while idx > 1 and self.arr[int(idx / 2)] < self.arr[idx]:
            self.arr[int(idx / 2)], self.arr[idx] = self.arr[idx], self.arr[int(idx / 2)]
            idx = int(idx / 2)

    def maximum(self):
        if self.size == 0:
            raise Exception('empty array')
        return self.arr[1]

    def max_heapify(self, i):
        left = 2 * i
        right = 2 * i + 1

        if left <= self.size() and self.arr[left] > self.arr[i]:
            largest = left
        else:
            largest = i

        if right <= self.size() and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)


a = [None, 8, 7, 4, 3, 1]

pq = Heap(a)
print(pq.arr)
pq.insert_value(6)
print(pq.arr)
