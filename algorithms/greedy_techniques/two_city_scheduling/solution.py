"""
production algorithm
"""


class Solution:
    def two_city_scheduling(self, costs):
        """
        time complexity O(nlogn)
        space complexity O(1)
        """
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs)
        result = 0

        for i in range(n):
            a, b = costs[i]
            if i < n / 2:
                result += a
            else:
                result += b

        return result
