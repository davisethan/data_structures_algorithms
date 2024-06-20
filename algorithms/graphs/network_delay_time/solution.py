"""
production algorithm
"""

from collections import defaultdict
from data_structures.heap.heap import Heap


class Solution:
    def network_delay_time(self, times, n, k):
        """
        time complexity O((V + E)logV)
        space complexity O(V + E)
        """
        # initialize directed weighted graph
        graph = defaultdict(list)
        for source, target, cost in times:
            graph[source], graph[target]
            graph[source].append((target, cost))
        if len(graph) < n:
            return -1

        # dijkstra's algorithm
        costs = {vertex: float("inf") for vertex in graph}
        costs[k] = 0
        heap = Heap()
        heap.push(MinHeapData(costs[k], k))
        while not heap.empty():
            minc, source = heap.pop()
            for target, cost in graph[source]:
                if minc + cost < costs[target]:
                    costs[target] = minc + cost
                    heap.push(MinHeapData(costs[target], target))

        # result
        minc = max([costs[v] for v in costs])
        if minc == float("inf"):
            return -1
        return minc


class MinHeapData:
    def __init__(self, cost, vertex):
        self.cost = cost
        self.vertex = vertex

    def __lt__(self, other):
        return self.cost < other.cost

    def __iter__(self):
        yield self.cost
        yield self.vertex

    def __len__(self):
        return 2
