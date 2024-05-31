"""
production algorithm
"""

from data_structures.heap.heap import Heap


class KthLargest:
    def __init__(self, k, numbers):
        """
        time complexity O(nlogk)
        space complexity O(k)
        """
        self.k = k
        self.heap = Heap()
        for i in range(len(numbers)):
            self.add(numbers[i])

    def add(self, value):
        """
        time complexity O(logk)
        space complexity O(1)
        """
        self.heap.push(value)
        if self.heap.size() > self.k:
            self.heap.pop()
        return self.heap.top()
