"""
unit tests
"""

from unittest import TestCase
from algorithms.top_k_elements.top_k_frequent_elements.solution import Solution


class SolutionTestCase(TestCase):
    def test_no_equal_frequencies(self):
        # Given
        numbers = [51, 53, 53, 55, 55, 55, 57, 57, 57, 57, 59, 59, 59, 59, 59]
        k = 3
        solution = Solution()

        # When
        actual = solution.top_k_frequent(numbers, k)

        # Then
        expected = [55, 57, 59]
        self.assertEqual(actual, expected)

    def test_some_equal_frequencies(self):
        # Given
        numbers = [51, 51, 51, 53, 53, 53, 53, 53, 55,
                   55, 55, 57, 57, 57, 57, 57, 59, 59, 59]
        k = 3
        solution = Solution()

        # When
        actual = solution.top_k_frequent(numbers, k)

        # Then
        expected = [59, 53, 57]
        self.assertEqual(actual, expected)
