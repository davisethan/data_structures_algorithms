"""
production algorithm
"""


class Solution:
    def find_k_sum_subsets(self, numbers, target):
        """
        time complexity O(n * 2^n)
        space complexity O(n)
        """
        n, i = len(numbers), 0
        current, result = list(), list()
        sum = 0
        self.get_k_sum_subsets_helper(
            numbers, target, n, i, sum, current, result)
        return result

    def get_k_sum_subsets_helper(self, numbers, target, n, i, sum, current, result):
        """
        time complexity O(n * 2^n)
        space complexity O(n)
        """
        if target < sum:
            return

        if sum == target:
            result.append(current[::])
            return

        for j in range(i, n):
            current.append(numbers[j])
            self.get_k_sum_subsets_helper(
                numbers, target, n, j + 1, sum + numbers[j], current, result)
            current.pop()
