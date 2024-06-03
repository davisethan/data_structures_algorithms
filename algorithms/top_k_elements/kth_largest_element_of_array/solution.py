"""
production algorithm
"""

from data_structures.heap.heap import Heap


class Solution:
    def find_kth_largest(self, numbers, k):
        """
        time complexity O(nlogk)
        space complexity O(k)
        """
        smallest = Heap()

        for i in range(len(numbers)):
            smallest.push(MinHeapData(numbers[i]))
            if k < smallest.size():
                smallest.pop()

        return smallest.top().number


class MinHeapData:
    def __init__(self, number):
        self.number = number

    def __lt__(self, other):
        return self.number < other.number
