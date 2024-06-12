"""
production algorithm
"""


class Solution:
    def distance(self, matrix):
        """
        time complexity O(mn)
        space complexity O(1)
        """
        m, n = len(matrix), len(matrix[0])
        result = [[float("inf") for _ in range(m)] for _ in range(n)]

        # forward
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                else:
                    up = 1 + result[i - 1][j] if 0 <= i - 1 else float("inf")
                    left = 1 + result[i][j - 1] if 0 <= j - 1 else float("inf")
                    result[i][j] = min(result[i][j], up, left)

        # backward
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                else:
                    down = 1 + result[i + 1][j] if i + 1 < m else float("inf")
                    right = 1 + result[i][j + 1] if j + 1 < n else float("inf")
                    result[i][j] = min(result[i][j], down, right)

        return result
