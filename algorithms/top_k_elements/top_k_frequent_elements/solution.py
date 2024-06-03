"""
production algorithm
"""

from collections import Counter
from data_structures.heap.heap import Heap


class Solution:
    def top_k_frequent(self, numbers, k):
        """
        time complexity O(n + mlogk)
        space complexity O(m + k)
        """
        counter = Counter(numbers)
        smallest = Heap()

        for number, count in counter.items():
            smallest.push(MinHeapData(count, number))
            if k < smallest.size():
                smallest.pop()

        result = list()
        for _ in range(k):
            _, number = smallest.pop()
            result.append(number)

        return result


class MinHeapData:
    def __init__(self, count, number):
        self.count = count
        self.number = number

    def __lt__(self, other):
        if self.count == other.count:
            return self.number < other.number
        return self.count < other.count

    def __iter__(self):
        yield self.count
        yield self.number

    def __len__(self):
        return 2
