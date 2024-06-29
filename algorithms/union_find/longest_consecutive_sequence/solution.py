"""
production algorithm
"""


class Solution:
    def longest_consecutive_sequence(self, numbers):
        """
        time complexity O(n)
        space complexity O(n)
        """
        unionfind = UnionFind(numbers)

        for number in numbers:
            if number + 1 in unionfind.parent:
                unionfind.union(number, number + 1)

        return unionfind.max_size


class UnionFind:
    def __init__(self, numbers):
        self.parent = {number: number for number in numbers}
        self.size = {number: 1 for number in numbers}
        self.max_size = 1

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
            if self.size[rootx] < self.size[rooty]:
                rooty, rootx = rootx, rooty
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
            self.max_size = max(self.max_size, self.size[rootx])
