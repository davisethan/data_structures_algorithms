"""
production algorithm
"""


class Solution:
    def find_subsets(self, numbers):
        """
        time complexity O(n * 2^n)
        space complexity O(n)
        """
        n, i = len(numbers), 0
        current, result = list(), list()
        self.find_subsets_helper(numbers, n, i, current, result)
        return result

    def find_subsets_helper(self, numbers, n, i, current, result):
        """
        time complexity O(n * 2^n)
        space complexity O(n)
        """
        result.append(current[::])
        for j in range(i, n):
            current.append(numbers[j])
            self.find_subsets_helper(numbers, n, j + 1, current, result)
            current.pop()
