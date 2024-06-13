"""
production algorithm
"""


class Solution:
    def climb_stairs(self, n):
        """
        time complexity O(n)
        space complexity O(n)
        """
        memo = [1 if k == 0 or k == 1 else None for k in range(n + 1)]

        for k in range(2, n + 1):
            memo[k] = memo[k - 1] + memo[k - 2]

        return memo[n]
