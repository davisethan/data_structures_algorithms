from data_structures.heap.heap import Heap


class DataStreamMedian:
    """
    store a stream of numbers and retrieve the median
    of all numbers seen so far in time complexity O(1)

    at least one number will be stored
    before the median is requested
    """

    def __init__(self):
        self.max_heap = Heap()
        self.min_heap = Heap()

    def insert(self, number):
        if self.max_heap.empty() or self.min_heap.empty():
            self.max_heap.push(MaxHeapData(number))
            self.rebalance()
            return
        if number < self.max_heap.top().number:
            self.max_heap.push(MaxHeapData(number))
            self.rebalance()
            return
        self.min_heap.push(MinHeapData(number))
        self.rebalance()

    def median(self):
        if self.max_heap.size() == self.min_heap.size():
            return (self.max_heap.top().number + self.min_heap.top().number) / 2
        if self.max_heap.size() < self.min_heap.size():
            return self.min_heap.top().number
        return self.max_heap.top().number

    def rebalance(self):
        if self.max_heap.size() + 2 == self.min_heap.size():
            number = self.min_heap.pop().number
            self.max_heap.push(MaxHeapData(number))
        if self.min_heap.size() + 2 == self.max_heap.size():
            number = self.max_heap.pop().number
            self.min_heap.push(MinHeapData(number))

    def __repr__(self):
        return f"(max_heap={self.max_heap}, min_heap={self.min_heap})"


class MinHeapData:
    def __init__(self, number):
        self.number = number

    def __lt__(self, other):
        return self.number < other.number

    def __repr__(self):
        return str(self.number)


class MaxHeapData:
    def __init__(self, number):
        self.number = number

    def __lt__(self, other):
        return other.number < self.number

    def __repr__(self):
        return str(self.number)
