"""
production algorithm
"""

from data_structures.heap.heap import Heap


class Solution:
    def k_smallest_number(self, lists, k):
        """
        time complexity O(klogn)
        space complexity O(n)
        """
        # add first number of each list to heap
        smallest = Heap()
        pointers = [0 for _ in range(len(lists))]
        for i in range(len(lists)):
            if 0 < len(lists[i]):
                smallest.push(MinHeapData(lists[i][pointers[i]], i))
        i, result = 0, list()

        while not smallest.empty() and i < k:
            # add number of list from heap to result
            number, index = smallest.pop()
            result.append(number)

            # add next number of list to heap
            pointers[index] = pointers[index] + 1
            if pointers[index] < len(lists[index]):
                smallest.push(MinHeapData(
                    lists[index][pointers[index]], index))

            i = i + 1

        if len(result) == 0:
            return 0
        return result[len(result) - 1]


class MinHeapData:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value < other.value

    def __iter__(self):
        yield self.value
        yield self.index

    def __len__(self):
        return 2
