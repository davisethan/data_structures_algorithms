"""
unit tests
"""

from unittest import TestCase
from algorithms.two_pointers.valid_palindrome_2.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_removals_succeeds(self):
        # Given
        string = "abcdefghhgfedcba"
        solution = Solution()

        # When
        actual = solution.is_palindrome(string)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_low_character_removal_succeeds(self):
        # Given
        string = "aabcdefghhgfedcba"
        solution = Solution()

        # When
        actual = solution.is_palindrome(string)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_high_character_removal_succeeds(self):
        # Given
        string = "abcdefghhgfedcbaa"
        solution = Solution()

        # When
        actual = solution.is_palindrome(string)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_low_character_removal_fails(self):
        # Given
        string = "aaabcdefghhgfedcba"
        solution = Solution()

        # When
        actual = solution.is_palindrome(string)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_high_character_removal_fails(self):
        # Given
        string = "abcdefghhgfedcbaaa"
        solution = Solution()

        # When
        actual = solution.is_palindrome(string)

        # Then
        expected = False
        self.assertEqual(actual, expected)
