"""
production algorithm
"""


class Solution:
    def find_missing_number(self, numbers):
        """
        time complexity O(n)
        space complexity O(1)
        """
        # sort
        n, i = len(numbers), 0
        while i < n:
            j = numbers[i]
            if 0 <= j < n and not numbers[i] == numbers[j]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
            else:
                i += 1

        # search
        for i in range(n):
            if not i == numbers[i]:
                return i
        return n
