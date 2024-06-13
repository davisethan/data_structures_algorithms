"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.palindromic_substrings.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_multi_character_palindromes(self):
        # Given
        string = "uvwxyz"
        solution = Solution()

        # When
        actual = solution.count_palindromic_substrings(string)

        # Then
        expected = 6
        self.assertEqual(actual, expected)

    def test_some_multi_character_palindromes(self):
        # Given
        string = "mnmmnm"
        solution = Solution()

        # When
        actual = solution.count_palindromic_substrings(string)

        # Then
        expected = 11
        self.assertEqual(actual, expected)

    def test_all_multi_character_palindromes(self):
        # Given
        string = "mmmmmm"
        solution = Solution()

        # When
        actual = solution.count_palindromic_substrings(string)

        # Then
        expected = 21
        self.assertEqual(actual, expected)
