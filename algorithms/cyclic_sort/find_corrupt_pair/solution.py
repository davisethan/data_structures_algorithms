"""
production algorithm
"""


class Solution:
    def find_corrupt_pair(self, numbers):
        """
        time complexity O(n)
        space complexity O(1)
        """
        # sort
        n, i = len(numbers), 0
        while i < n:
            j = numbers[i] - 1
            if not i == j and not numbers[i] == numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                i += 1

        # search
        for i in range(n):
            if not i == numbers[i] - 1:
                return [i + 1, numbers[i]]
