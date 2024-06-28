"""
production algorithm
"""


class Solution:
    def number_of_islands(self, grid):
        """
        time complexity O(mn)
        space complexity O(mn)
        """
        water, land = 0, 1
        m, n = len(grid), len(grid[0])
        unionfind = UnionFind(m * n)

        # exlcude water cells
        # reduce count of representatives
        for row in range(m):
            for column in range(n):
                if grid[row][column] == water:
                    unionfind.count -= 1

        # union land cells
        # reduce count of representatives
        for row in range(m):
            for column in range(n):
                if grid[row][column] == land:
                    if row < m - 1 and grid[row + 1][column] == land:
                        unionfind.union(row * n + column,
                                        (row + 1) * n + column)
                    if column < n - 1 and grid[row][column + 1] == land:
                        unionfind.union(row * n + column,
                                        row * n + (column + 1))

        return unionfind.count


class UnionFind:
    def __init__(self, size):
        self.parent = [n for n in range(size + 1)]
        self.size = [1 for _ in range(size + 1)]
        self.count = size

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
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            else:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            self.count -= 1
