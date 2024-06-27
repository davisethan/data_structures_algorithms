"""
unit tests
"""

from unittest import TestCase
from algorithms.counters.first_unique_character_in_string.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_unique_characters(self):
        # Given
        string = "uuuvvvwwwxxxyyyzzz"
        solution = Solution()

        # When
        actual = solution.first_unique_character(string)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_some_unique_characters(self):
        # Given
        string = "rstuuuvvvwwwxxxyyyzzz"
        solution = Solution()

        # When
        actual = solution.first_unique_character(string)

        # Then
        expected = 0
        self.assertEqual(actual, expected)
