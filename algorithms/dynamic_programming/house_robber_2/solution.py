"""
production algorithm
"""


class Solution:
    def house_robber(self, money):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if len(money) == 1:
            return money[0]

        return max(
            self.house_robber_helper(money[:-1]),
            self.house_robber_helper(money[1:]))

    def house_robber_helper(self, money):
        """
        time complexity O(n)
        space complexity O(n)
        """
        n = len(money)
        memo = [0 if k == 0 else None for k in range(n + 1)]

        for k in range(1, n + 1):
            if 0 <= k - 2:
                memo[k] = max(money[k - 1] + memo[k - 2], memo[k - 1])
            else:
                memo[k] = max(money[k - 1], memo[k - 1])

        return memo[n]
