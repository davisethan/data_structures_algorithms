"""
production algorithm
"""


class Solution:
    def word_search(self, grid, word):
        """
        time complexity O(m * n * 4^k)
        space complexity O(k)
        """
        m, n = len(grid), len(grid[0])
        k, i = len(word), 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = [False]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == word[0]:
                    self.word_search_helper(
                        grid, m, n, word, k, i, row, col, directions, result)

        return result[0]

    def word_search_helper(self, grid, m, n, word, k, i, row, col, directions, result):
        """
        time complexity O(4^k)
        space complexity O(k)
        """
        # base case
        if result[0]:
            return

        # base case
        if i == k:
            result[0] = True
            return

        # base case
        if row < 0 or row == m:
            return

        # base case
        if col < 0 or col == n:
            return

        # base case
        if not grid[row][col] == word[i]:
            return

        for x, y in directions:
            self.word_search_helper(
                grid, m, n, word, k, i + 1, row + x, col + y, directions, result)
