"""
production algorithm
"""


class Solution:
    def max_profit(self, capacity, weights, values):
        """
        time complexity O(nc)
        space complexity O(nc)
        """
        n = len(weights)
        memo = [[0 if m == 0 or c == 0 else None for c in range(
            capacity + 1)] for m in range(n + 1)]
        
        for m in range(1, n + 1):
            for c in range(1, capacity + 1):
                if weights[m - 1] <= c:
                    memo[m][c] = max(
                        values[m - 1] + memo[m - 1][c - weights[m - 1]],
                        memo[m - 1][c])
                else:
                    memo[m][c] = memo[m - 1][c]

        return memo[n][capacity]
