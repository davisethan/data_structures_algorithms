"""
production algorithm
"""

from data_structures.heap.heap import Heap


class Solution:
    def minimum_refuel_stops(self, target, fuel, stations):
        """
        time complexity O(nlogn)
        space complexity O(n)
        """
        if target <= fuel:
            return 0

        n = len(stations)
        current = fuel
        refuel = Heap()

        for i in range(n):
            distance, next = stations[i]
            while current < distance:
                if refuel.empty():
                    return -1
                current += refuel.pop().data
            refuel.push(MaxHeapData(next))

        while current < target:
            if refuel.empty():
                return -1
            current += refuel.pop().data
        return n - refuel.size()


class MaxHeapData:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return other.data < self.data
