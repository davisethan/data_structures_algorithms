"""
production algorithm
"""

from collections import defaultdict


class Solution:
    def valid_tree(self, n, edges):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if not len(edges) == n - 1:
            return False

        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        root = n - 1
        visited = set()
        stack = list()
        stack.append(root)

        while stack:
            node = stack.pop()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return len(visited) == n
