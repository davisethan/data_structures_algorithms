"""
production algorithm
"""

from math import floor, log


class Solution:
    def counting_bits(self, n):
        """
        time complexity O(n)
        space complexity O(n)
        """
        memo = [0 if k == 0 else None for k in range(n + 1)]

        for k in range(1, n + 1):
            memo[k] = 1 + memo[k - 2**floor(log(k, 2))]

        return memo
