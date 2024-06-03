"""
production algorithm
"""

from math import sqrt
from data_structures.heap.heap import Heap


class Solution:
    def k_closest(self, points, k):
        """
        time complexity O(nlogk)
        space complexity O(k)
        """
        closest = Heap()
        for i in range(len(points)):
            closest.push(MaxHeapData(self.distance(points[i]), points[i]))
            if k < closest.size():
                closest.pop()

        result = list()
        for i in range(k):
            _, point = closest.pop()
            result.append(point)

        return result

    def distance(self, point):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return sqrt(point.x ** 2 + point.y ** 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MaxHeapData:
    def __init__(self, distance, point):
        self.distance = distance
        self.point = point

    def __lt__(self, other):
        return other.distance < self.distance

    def __iter__(self):
        yield self.distance
        yield self.point

    def __len__(self):
        return 2
