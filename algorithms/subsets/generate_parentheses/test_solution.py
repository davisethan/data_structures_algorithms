"""
unit tests
"""

from unittest import TestCase
from algorithms.subsets.generate_parentheses.solution import Solution


class SolutionTestCase(TestCase):
    def test_one_pair_of_parentheses(self):
        # Given
        n = 1
        solution = Solution()

        # When
        generated = solution.generate_combinations(n)
        actual = set(generated)

        # Then
        expected = {"()"}
        self.assertEqual(actual, expected)

    def test_two_pairs_of_parentheses(self):
        # Given
        n = 2
        solution = Solution()

        # When
        generated = solution.generate_combinations(n)
        actual = set(generated)

        # Then
        expected = {"()()", "(())"}
        self.assertEqual(actual, expected)

    def test_three_pairs_of_parentheses(self):
        # Given
        n = 3
        solution = Solution()

        # When
        generated = solution.generate_combinations(n)
        actual = set(generated)

        # Then
        expected = {"()()()", "(())()", "()(())", "(()())", "((()))"}
        self.assertEqual(actual, expected)
