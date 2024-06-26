"""
unit tests
"""

from unittest import TestCase
from algorithms.counters.palindrome_permutation.solution import Solution


class SolutionTestCase(TestCase):
    def test_permute_palindrome_fails(self):
        # Given
        string = "uvvwwwxxxxyyyyyzzzzzz"
        solution = Solution()

        # When
        actual = solution.permute_palindrome(string)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_permute_palindrome_succeeds(self):
        # Given
        string = "wwxxxxyyyyyyzzzzzzzz"
        solution = Solution()

        # When
        actual = solution.permute_palindrome(string)

        # Then
        expected = True
        self.assertEqual(actual, expected)
