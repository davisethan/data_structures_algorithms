"""
production algorithm
"""

from collections import defaultdict
from data_structures.queue.queue import Queue


class Solution:
    def alien_order(self, words):
        """
        time complexity O(c)
        space complexity O(1)
        """
        # initialize graph vertexes
        n = len(words)
        graph = defaultdict(list)
        for i in range(n):
            m = len(words[i])
            for j in range(m):
                graph[words[i][j]]

        # initialize graph edges
        for i in range(1, n):
            p, q = len(words[i - 1]), len(words[i])
            m = min(p, q)
            d = False
            for j in range(m):
                if not words[i - 1][j] == words[i][j]:
                    graph[words[i - 1][j]].append(words[i][j])
                    d = True
                    break
            if not d and q < p:
                return str()

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

        # sort vertexes
        ordered = list()
        while not queue.empty():
            v = queue.pop()
            ordered.append(v)
            for u in graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.push(u)

        if len(ordered) == len(graph):
            return "".join(ordered)
        return str()
