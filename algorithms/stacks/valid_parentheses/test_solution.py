"""
unit tests
"""

from unittest import TestCase
from algorithms.stacks.valid_parentheses.solution import Solution


class SolutionTestCase(TestCase):
    def test_all_valid_parentheses(self):
        # Given
        string = "{[(()[]{})]}"
        solution = Solution()

        # When
        actual = solution.is_valid(string)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_some_invalid_parentheses(self):
        # Given
        string = "}])()[]{}([{"
        solution = Solution()

        # When
        actual = solution.is_valid(string)

        # Then
        expected = False
        self.assertEqual(actual, expected)
