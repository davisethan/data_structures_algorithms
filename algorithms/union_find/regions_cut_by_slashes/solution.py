"""
production algorithm
"""


class Solution:
    def regions_cut_by_slashes(self, grid):
        """
        time complexity O(mn)
        space complexity O(mn)
        """
        whitespace, backslash, forwardslash = "w", "b", "f"
        grid = [row.replace(" ", whitespace)
                .replace("\\", backslash)
                .replace("/", forwardslash) for row in grid]
        rows, columns = len(grid), len(grid[0])
        size = rows * columns * 4
        unionfind = UnionFind(size)

        for row in range(rows):
            for column in range(columns):
                # connect regions of single square
                north = self.get_north(row, column, columns)
                east, south, west = north + 1, north + 2, north + 3
                if grid[row][column] == whitespace:
                    unionfind.union(north, east)
                    unionfind.union(east, south)
                    unionfind.union(south, west)
                if grid[row][column] == backslash:
                    unionfind.union(north, east)
                    unionfind.union(south, west)
                if grid[row][column] == forwardslash:
                    unionfind.union(north, west)
                    unionfind.union(east, south)

                # interconnect regions of multiple squares
                next_north = south + self.get_next_north_distance(columns)
                next_west = east + 6
                if column < columns - 1:
                    unionfind.union(east, next_west)
                if row < rows - 1:
                    unionfind.union(south, next_north)

        return unionfind.count

    def get_north(self, row, column, columns):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return (row * columns * 4) + (column * 4)

    def get_next_north_distance(self, columns):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.get_north(1, 0, columns) - 2


class UnionFind:
    def __init__(self, size):
        self.parent = [n for n in range(size)]
        self.size = [1 for _ in range(size)]
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
                rooty, rootx = rootx, rooty
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
            self.count -= 1
