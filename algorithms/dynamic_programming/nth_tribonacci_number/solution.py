"""
production algorithm
"""


class Solution:
    def tribonacci(self, n):
        """
        time complexity O(n)
        space complexity O(1)
        """
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        ta, tb, tc = 0, 1, 1
        for _ in range(3, n + 1):
            ta, tb, tc = tb, tc, ta + tb + tc
        return tc
