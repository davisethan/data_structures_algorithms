"""
unit tests
"""

from unittest import TestCase
from algorithms.cyclic_sort.missing_number.solution import Solution


class SolutionTestCase(TestCase):
    def test_first_integer_missing(self):
        # Given
        numbers = [8, 9, 10, 11, 12, 13, 14, 15,
                   16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7]
        solution = Solution()

        # When
        actual = solution.find_missing_number(numbers)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_last_integer_missing(self):
        # Given
        numbers = [8, 9, 10, 11, 12, 13, 14, 15,
                   16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7]
        solution = Solution()

        # When
        actual = solution.find_missing_number(numbers)

        # Then
        expected = 20
        self.assertEqual(actual, expected)

    def test_some_middle_integer_missing(self):
        # Given
        numbers = [8, 9, 10, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 0, 1, 2, 3, 4, 5, 6, 7]
        solution = Solution()

        # When
        actual = solution.find_missing_number(numbers)

        # Then
        expected = 11
        self.assertEqual(actual, expected)
