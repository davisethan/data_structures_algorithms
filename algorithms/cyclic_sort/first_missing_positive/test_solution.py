"""
unit tests
"""

from unittest import TestCase
from algorithms.cyclic_sort.first_missing_positive.solution import Solution


class SolutionTestCase(TestCase):
    def test_smallest_positive_integer_missing(self):
        # Given
        numbers = [13, 2, 9, 6, 11, 19, 5, 17, 20,
                   15, 10, 8, 7, 4, 18, 14, 3, 12, 16]
        solution = Solution()

        # When
        actual = solution.smallest_missing_positive_integer(numbers)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_middle_positive_integer_missing(self):
        # Given
        numbers = [13, 2, 9, 6, 19, 5, 17, 20,
                   15, 10, 8, 7, 4, 18, 1, 14, 3, 12, 16]
        solution = Solution()

        # When
        actual = solution.smallest_missing_positive_integer(numbers)

        # Then
        expected = 11
        self.assertEqual(actual, expected)

    def test_largest_positive_integer_missing(self):
        # Given
        numbers = [13, 2, 9, 6, 11, 19, 5, 17, 15,
                   25, 10, 8, 7, 4, 18, 1, 14, 3, 12, 16]
        solution = Solution()

        # When
        actual = solution.smallest_missing_positive_integer(numbers)

        # Then
        expected = 20
        self.assertEqual(actual, expected)
