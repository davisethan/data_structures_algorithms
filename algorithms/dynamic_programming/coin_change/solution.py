"""
production algorithm
"""


class Solution:
    def coin_change(self, coins, total):
        """
        time complexity O(tc)
        space complexity O(t)
        """
        memo = [0 if t == 0 else None for t in range(total + 1)]

        for t in range(1, total + 1):
            k = float("inf")
            for c in coins:
                if c <= t:
                    k = min(k, 1 + memo[t - c])
            memo[t] = k

        if memo[total] == float("inf"):
            return -1
        return memo[total]
