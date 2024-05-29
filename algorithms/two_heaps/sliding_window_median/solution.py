"""
production algorithm
"""


from collections import defaultdict
from data_structures.heap.heap import Heap


class Solution:
    def median_sliding_window(self, nums, k):
        low, high = Heap(), Heap()
        visited = defaultdict(int)
        result = list()

        # build window
        for i in range(k):
            low.push(MaxHeapData(nums[i]))
        for i in range(k // 2):
            high.push(MinHeapData(low.pop().data))

        # record result
        if k % 2 == 0:
            result.append(low.top().data / 2 + high.top().data / 2)
        else:
            result.append(low.top().data)

        # slide window
        for i in range(k, len(nums)):

            # stage pop of low index of window
            balance = 0
            visited[nums[i - k]] += 1
            if nums[i - k] <= low.top().data:
                balance -= 1
            else:
                balance += 1

            # push high index of window
            if nums[i] <= low.top().data:
                low.push(MaxHeapData(nums[i]))
                balance += 1
            else:
                high.push(MinHeapData(nums[i]))
                balance -= 1

            # rebalance window
            if balance < 0:
                low.push(MaxHeapData(high.pop().data))
            if 0 < balance:
                high.push(MinHeapData(low.pop().data))

            # pop staged low indexes of window
            while not low.empty() and 0 < visited[low.top().data]:
                visited[low.top().data] -= 1
                low.pop()
            while not high.empty() and 0 < visited[high.top().data]:
                visited[high.top().data] -= 1
                high.pop()

            # record result
            if k % 2 == 0:
                result.append(low.top().data / 2 + high.top().data / 2)
            else:
                result.append(low.top().data)

        return result


class MinHeapData:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data < other.data


class MaxHeapData:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return other.data < self.data
