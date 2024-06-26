"""
unit tests
"""

from unittest import TestCase
from algorithms.hashmaps.longest_palindrome.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_odd_number_of_character_occurrences(self):
        # Given
        s = "wwxxxxyyyyyyzzzzzzzz"
        solution = Solution()

        # When
        actual = solution.longest_palindrome(s)

        # Then
        expected = 20
        self.assertEqual(actual, expected)

    def test_some_odd_number_of_character_occurrences(self):
        # Given
        s = "uvvwwwxxxxyyyyyzzzzzz"
        solution = Solution()

        # When
        actual = solution.longest_palindrome(s)

        # Then
        expected = 19
        self.assertEqual(actual, expected)
