"""
production algorithm
"""

from data_structures.heap.heap import Heap


class Solution:
    def k_smallest_pairs(self, list1, list2, k):
        """
        time complexity O(klogn)
        space complexity O(n)
        """
        # add to heap sum of each value of first list
        # and first value of second list
        smallest = Heap()
        [smallest.push(MinHeapData(list1[i] + list2[0], i, 0))
         for i in range(len(list1))]
        i, result = 0, list()

        while not smallest.empty() and i < k:
            _, index1, index2 = smallest.pop()
            result.append((list1[index1], list2[index2]))

            # add to heap sum of value of first list
            # and next value of second list
            if index2 + 1 < len(list2):
                smallest.push(MinHeapData(
                    list1[index1] + list2[index2 + 1], index1, index2 + 1))

            i = i + 1

        return result


class MinHeapData:
    def __init__(self, sum, index1, index2):
        self.sum = sum
        self.index1 = index1
        self.index2 = index2

    def __lt__(self, other):
        return self.sum < other.sum

    def __iter__(self):
        yield self.sum
        yield self.index1
        yield self.index2

    def __len__(self):
        return 3
