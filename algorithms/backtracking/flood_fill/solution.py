"""
production algorithm
"""


class Solution:
    def flood_fill(self, grid, sr, sc, target):
        """
        time complexity O(mn)
        space complexity O(mn)
        """
        if grid[sr][sc] == target:
            return grid

        m, n = len(grid), len(grid[0])
        origin = grid[sr][sc]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.flood_fill_helper(grid, m, n, sr, sc, target, origin, directions)
        return grid

    def flood_fill_helper(self, grid, m, n, sr, sc, target, origin, directions):
        """
        time complexity O(mn)
        space complexity O(mn)
        """
        # base case
        if sr < 0 or sr == m:
            return

        # base case
        if sc < 0 or sc == n:
            return

        # base case
        if not grid[sr][sc] == origin:
            return

        grid[sr][sc] = target
        for x, y in directions:
            self.flood_fill_helper(
                grid, m, n, sr + x, sc + y, target, origin, directions)
