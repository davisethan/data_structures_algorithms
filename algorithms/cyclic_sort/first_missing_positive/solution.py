"""
production algorithm
"""


class Solution:
    def smallest_missing_positive_integer(self, numbers):
        """
        time complexity O(n)
        space complexity O(1)
        """
        # sort
        n, i = len(numbers), 0
        while i < n:
            j = numbers[i] - 1
            if 0 <= j < n and not numbers[i] == numbers[j]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
            else:
                i += 1

        # search
        for i in range(n):
            j = numbers[i] - 1
            if not i == j:
                return i + 1
        return n
