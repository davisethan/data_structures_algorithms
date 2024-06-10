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
        current, next = 0, 0
        count = 0

        for i in range(n):
            if current < i:
                current, next = next, i + numbers[i]
                count += 1
            next = max(next, i + numbers[i])

        return count
