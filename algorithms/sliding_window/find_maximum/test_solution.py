"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.find_maximum.solution import Solution


class SolutionTestCase(TestCase):
    def test_strictly_increasing_numbers(self):
        # Given
        numbers = [51, 53, 55, 57, 59, 61, 63, 65, 67, 69]
        size = 3
        solution = Solution()

        # When
        actual = solution.find_maximum(numbers, size)

        # Then
        expected = [55, 57, 59, 61, 63, 65, 67, 69]
        self.assertEqual(actual, expected)

    def test_strictly_decreasing_numbers(self):
        # Given
        numbers = [69, 67, 65, 63, 61, 59, 57, 55, 53, 51]
        size = 3
        solution = Solution()

        # When
        actual = solution.find_maximum(numbers, size)

        # Then
        expected = [69, 67, 65, 63, 61, 59, 57, 55]
        self.assertEqual(actual, expected)

    def test_constant_numbers(self):
        # Given
        numbers = [51, 51, 51, 51, 51, 51, 51, 51, 51, 51]
        size = 3
        solution = Solution()

        # When
        actual = solution.find_maximum(numbers, size)

        # Then
        expected = [51, 51, 51, 51, 51, 51, 51, 51]
        self.assertEqual(actual, expected)

    def test_worst_case_numbers(self):
        # Given
        numbers = [51, 51, 51, 53, 53, 53, 55, 55, 55, 57]
        size = 3
        solution = Solution()

        # When
        actual = solution.find_maximum(numbers, size)

        # Then
        expected = [51, 53, 53, 53, 55, 55, 55, 57]
        self.assertEqual(actual, expected)
