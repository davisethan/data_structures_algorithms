"""
production algorithm
"""


class Solution:
    def jump_game(self, numbers):
        """
        time complexity O(n)
        space complexity O(1)
        """
        n = len(numbers)
        available = float("-inf")

        for i in range(0, n - 1):
            available = max(available - 1, numbers[i])
            if available == 0:
                return False

        return True
