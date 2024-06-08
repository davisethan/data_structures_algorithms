"""
production algorithm
"""


class Solution:
    def journey(self, gas, cost):
        """
        time complexity O(n)
        space complexity O(1)
        """
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        tank, index = 0, 0

        for i in range(n):
            if tank + gas[i] - cost[i] < 0:
                tank, index = 0, i + 1
            else:
                tank += gas[i] - cost[i]

        return index
