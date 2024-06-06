"""
unit tests
"""

from unittest import TestCase
from algorithms.subsets.subsets.solution import Solution


class SolutionTestCase(TestCase):
    def test_single_element_array(self):
        # Given
        numbers = [1]
        solution = Solution()

        # When
        subsets = solution.find_subsets(numbers)
        actual = {tuple(subset) for subset in subsets}

        # Then
        expected = {tuple([]), tuple([1])}
        self.assertEqual(actual, expected)

    def test_multi_element_array(self):
        # Given
        numbers = [1, 3, 5]
        solution = Solution()

        # When
        subsets = solution.find_subsets(numbers)
        actual = {tuple(subset) for subset in subsets}

        # Then
        expected = {tuple([]), tuple([1]), tuple([3]), tuple([5]), tuple(
            [1, 3]), tuple([1, 5]), tuple([3, 5]), tuple([1, 3, 5])}
        self.assertEqual(actual, expected)
