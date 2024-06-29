"""
unit tests
"""

from unittest import TestCase
from algorithms.union_find.longest_consecutive_sequence.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_consecutive_integers(self):
        # Given
        numbers = [-44, -31, -12, 7, 18, -40, 25, -16, 33,
                   10, -27, 36, -3, 14, -20, 42, -8, 20, -37, 28]
        solution = Solution()

        # When
        actual = solution.longest_consecutive_sequence(numbers)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_some_consecutive_integers(self):
        # Given
        numbers = [-44, -42, -12, -41, 18, -40, 25, -43, -
                   10, 10, 11, 9, 12, 14, -20, 42, -8, -9, -7, 28]
        solution = Solution()

        # When
        actual = solution.longest_consecutive_sequence(numbers)

        # Then
        expected = 5
        self.assertEqual(actual, expected)

    def test_all_consecutive_integers(self):
        # Given
        numbers = [-10, -9, -8, -7, -6, -5, -4, -
                   3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        solution = Solution()

        # When
        actual = solution.longest_consecutive_sequence(numbers)

        # Then
        expected = 20
        self.assertEqual(actual, expected)
