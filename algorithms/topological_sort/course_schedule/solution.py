"""
production algorithm
"""

from collections import defaultdict
from data_structures.queue.queue import Queue


class Solution:
    def find_order(self, n, prerequisites):
        """
        time complexity O(V + E)
        space complexity O(V + E)
        """
        # initialize graph vertexes
        graph = defaultdict(list)
        for m in range(n):
            graph[m]

        # initialize graph edges
        for child, parent in prerequisites:
            graph[parent].append(child)

        # initialize indegree counter
        indegree = defaultdict(int)
        for v in graph:
            indegree[v]
            for u in graph[v]:
                indegree[u] += 1

        # initialize bfs queue
        queue = Queue()
        for v in indegree:
            if indegree[v] == 0:
                queue.push(v)

        # sort
        ordered = list()
        while not queue.empty():
            v = queue.pop()
            ordered.append(v)
            for u in graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.push(u)

        if len(ordered) == len(graph):
            return ordered
        return list()
