"""
production algorithm
"""


class Solution:
    def max_profit(self, prices):
        """
        time complexity O(n)
        space complexity O(1)
        """
        length, low, high = len(prices), 0, 0
        profit = float("-inf")

        # step forward high index
        for high in range(length):
            profit = max(profit, prices[high] - prices[low])

            # step forward low index
            if prices[high] - prices[low] < 0:
                low = high

        if profit == float("-inf"):
            return 0
        return profit
