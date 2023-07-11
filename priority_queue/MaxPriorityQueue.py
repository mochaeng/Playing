# ------------- Article --------------------
# https://pages.cs.wisc.edu/~vernon/cs367/notes/11.PRIORITY-Q.html

class PriorityQueue:

    def __init__(self):
        self.heap = []

    def top(self):
        if len(self) == 0:
            raise IndexError('front from empty queue')
        return self.heap[0]

    def push(self, item) -> None:
        self.heap.append(item)

        current_idx = len(self) - 1
        while current_idx > 0:
            parent = self.find_parent(current_idx)
            if parent is not None and self.heap[current_idx] >= self.heap[parent]:
                self.__swap(current_idx, parent)
            current_idx = self.find_parent(current_idx)

    def pop(self):
        top = self.top()
        self.heap[0] = self.heap[-1]
        del self.heap[-1]

        current_idx = 0
        while True:
            left = self.find_left(current_idx)
            right = self.find_right(current_idx)

            if left is not None and self.heap[left] >= self.heap[current_idx]:
                largest = left
            else:
                largest = current_idx

            if right is not None and self.heap[right] >= self.heap[largest]:
                largest = right

            if current_idx == largest:
                break

            self.__swap(current_idx, largest)
            current_idx = largest

        return top

    def empty(self) -> bool:
        return len(self) == 0

    def __swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def __len__(self) -> int:
        return len(self.heap)

    def find_parent(self, idx):
        value = (idx - 1) // 2
        return value if value < len(self) else None

    def find_left(self, idx):
        value = (idx * 2) + 1
        return value if value < len(self) else None

    def find_right(self, idx):
        value = (idx * 2) + 2
        return value if value < len(self) else None

    def __str__(self):
        string = '{'
        for item in self.heap:
            string += str(item.priority)
            string += ','

        string += '}'
        return string
