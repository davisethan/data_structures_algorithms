"""
unit tests
"""

from unittest import TestCase
from algorithms.subsets.find_k_sum_subsets.solution import Solution


class SolutionTestCase(TestCase):
    def test_no_k_sum_subsets(self):
        # Given
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 55
        solution = Solution()

        # When
        subsets = solution.find_k_sum_subsets(numbers, target)
        actual = {tuple(subset) for subset in subsets}

        # Then
        expected = set()
        self.assertEqual(actual, expected)

    def test_some_k_sum_subsets(self):
        # Given
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10
        solution = Solution()

        # When
        subsets = solution.find_k_sum_subsets(numbers, target)
        actual = {tuple(subset) for subset in subsets}

        # Then
        expected = {tuple([1, 2, 3, 4]), tuple([1, 2, 7]), tuple([1, 3, 6]), tuple([1, 4, 5]), tuple([1, 9]),
                    tuple([2, 3, 5]), tuple([2, 8]), tuple([3, 7]), tuple([4, 6])}
        self.assertEqual(actual, expected)
