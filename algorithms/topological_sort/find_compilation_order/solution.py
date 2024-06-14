"""
production algorithm
"""

from collections import defaultdict
from data_structures.queue.queue import Queue


class Solution:
    def find_compilation_order(self, dependencies):
        """
        time complexity O(E + V)
        space complexity O(E + V)
        """
        # initialize graph as adjacency list
        graph = defaultdict(list)
        for child, parent in dependencies:
            graph[child], graph[parent].append(child)

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
