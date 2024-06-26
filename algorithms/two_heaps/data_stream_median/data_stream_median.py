"""
production algorithm
"""

from data_structures.heap.heap import Heap


class DataStreamMedian:
    def __init__(self):
        self.low = Heap()
        self.high = Heap()

    def insert(self, number):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        if self.low.empty() or self.high.empty():
            self.low.push(MaxHeapData(number))
            self.rebalance()
            return
        if number <= self.low.top().data:
            self.low.push(MaxHeapData(number))
            self.rebalance()
            return
        self.high.push(MinHeapData(number))
        self.rebalance()

    def median(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if self.low.size() == self.high.size():
            return self.low.top().data / 2 + self.high.top().data / 2
        return self.low.top().data

    def rebalance(self):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        if self.low.size() < self.high.size():
            data = self.high.pop().data
            self.low.push(MaxHeapData(data))
        if self.high.size() + 1 < self.low.size():
            data = self.low.pop().data
            self.high.push(MinHeapData(data))

    def __repr__(self):
        return f"(maxheap={self.low}, minheap={self.high})"


class MinHeapData:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data < other.data

    def __repr__(self):
        return str(self.data)


class MaxHeapData:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return other.data < self.data

    def __repr__(self):
        return str(self.data)
