"""
production algorithm
"""


class Solution:
    def redundant_connection(self, edges):
        """
        time complexity O(n)
        space complexity O(n)
        """
        size = float("-inf")
        for u, v in edges:
            size = max(size, u, v)
        unionfind = UnionFind(size)
        result = []

        for u, v in edges:
            if unionfind.connected(u, v):
                result = [u, v]
            unionfind.union(u, v)

        return result


class UnionFind:
    def __init__(self, size):
        self.parent = [n for n in range(size + 1)]
        self.rank = [1 for _ in range(size + 1)]

    def find(self, x):
        """
        time complexity O(⍺(n))
        space complexity O(n)
        """
        if not self.parent[x] == x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        time complexity O(⍺(n))
        space complexity O(n)
        """
        rootx = self.find(x)
        rooty = self.find(y)

        if not rootx == rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            elif self.rank[rooty] < self.rank[rootx]:
                self.parent[rooty] = rootx
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

    def connected(self, x, y):
        """
        time complexity O(⍺(n))
        space complexity O(n)
        """
        return self.find(x) == self.find(y)
