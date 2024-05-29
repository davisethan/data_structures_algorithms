"""
production algorithm
"""

from data_structures.heap.heap import Heap


class Solution:
    def minimum_machines(self, tasks):
        """
        time complexity O(nlogn)
        space complexity O(n)
        """
        start_times, end_times = Heap(), Heap()

        for task in tasks:
            start_times.push(task)
        _, end = start_times.pop()
        end_times.push(end)

        while not start_times.empty():
            start, end = start_times.pop()
            if end_times.top() <= start:
                end_times.pop()
            end_times.push(end)

        return end_times.size()
