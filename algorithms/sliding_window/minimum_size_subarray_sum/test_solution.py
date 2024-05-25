"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.minimum_size_subarray_sum.solution import Solution


class SolutionTestCase(TestCase):
    def test_empty_numbers(self):
        # Given
        numbers = []
        target = 20
        solution = Solution()

        # When
        actual = solution.minimum_size_subarray_sum(numbers, target)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_numbers_less_than_target(self):
        # Given
        numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        target = 100
        solution = Solution()

        # When
        actual = solution.minimum_size_subarray_sum(numbers, target)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_numbers_greater_than_target(self):
        # Given
        numbers = [12, 14, 16, 18, 20]
        target = 10
        solution = Solution()

        # When
        actual = solution.minimum_size_subarray_sum(numbers, target)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_constant_window(self):
        # Given
        numbers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        target = 20
        solution = Solution()

        # When
        actual = solution.minimum_size_subarray_sum(numbers, target)

        # Then
        expected = 4
        self.assertEqual(actual, expected)

    def test_dynamic_window(self):
        # Given
        numbers = [5, 5, 5, 5, 10, 10, 3, 7, 2, 8]
        target = 20
        solution = Solution()

        # When
        actual = solution.minimum_size_subarray_sum(numbers, target)

        # Then
        expected = 2
        self.assertEqual(actual, expected)
