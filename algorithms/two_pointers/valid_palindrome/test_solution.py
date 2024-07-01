"""
unit tests
"""

from unittest import TestCase
from algorithms.two_pointers.valid_palindrome.solution import Solution


class SolutionTestCase(TestCase):
    def test_is_palindrome_fails(self):
        # Given
        string = "abcdefghxyhgfedcba"
        solution = Solution()

        # When
        actual = solution.is_palindrome(string)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_is_palindrome_succeeds(self):
        # Given
        string = "abcdefghhgfedcba"
        solution = Solution()

        # When
        actual = solution.is_palindrome(string)

        # Then
        expected = True
        self.assertEqual(actual, expected)
