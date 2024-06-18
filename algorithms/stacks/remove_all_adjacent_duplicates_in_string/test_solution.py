"""
unit tests
"""

from unittest import TestCase
from algorithms.stacks.remove_all_adjacent_duplicates_in_string.solution import Solution


class SolutionTestCase(TestCase):
    def test_duplicates_removed(self):
        # Given
        string = "wxxyyz"
        solution = Solution()

        # When
        actual = solution.remove_duplicates(string)

        # Then
        expected = "wz"
        self.assertEqual(actual, expected)

    def test_duplicates_separated_by_duplicates_removed(self):
        # Given
        string = "uvwwvxyyxz"
        solution = Solution()

        # When
        actual = solution.remove_duplicates(string)

        # Then
        expected = "uz"
        self.assertEqual(actual, expected)
