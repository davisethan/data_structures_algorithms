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
            if not i == j and 0 <= j < n:
                numbers[j], numbers[i] = numbers[i], numbers[j]
            else:
                i += 1

        # search
        for i in range(n):
            if not i == numbers[i]:
                return i
        return n
