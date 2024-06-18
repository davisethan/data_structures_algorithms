"""
unit tests
"""

from unittest import TestCase
from algorithms.stacks.minimum_remove_to_make_valid_parentheses.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_unmatched_parentheses(self):
        # Given
        string = "kt(mnls)hwg(pu(ax)ie)"
        solution = Solution()

        # When
        actual = solution.min_remove_parentheses(string)

        # Then
        expected = "kt(mnls)hwg(pu(ax)ie)"
        self.assertEqual(actual, expected)

    def test_some_unmatched_parentheses(self):
        # Given
        string = "kt(mnls)hwg)pu(ax)ie("
        solution = Solution()

        # When
        actual = solution.min_remove_parentheses(string)

        # Then
        expected = "kt(mnls)hwgpu(ax)ie"
        self.assertEqual(actual, expected)

    def test_all_unmatched_parentheses(self):
        # Given
        string = ")))))((((("
        solution = Solution()

        # When
        actual = solution.min_remove_parentheses(string)

        # Then
        expected = ""
        self.assertEqual(actual, expected)
