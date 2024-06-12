"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.nth_tribonacci_number.solution import Solution


class SolutionTestCase(TestCase):
    def test_n_is_base_case_zero(self):
        # Given
        n = 0
        solution = Solution()

        # When
        actual = solution.tribonacci(n)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_n_is_base_case_one(self):
        # Given
        n = 1
        solution = Solution()

        # When
        actual = solution.tribonacci(n)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_n_is_base_case_two(self):
        # Given
        n = 2
        solution = Solution()

        # When
        actual = solution.tribonacci(n)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_n_is_not_base_case(self):
        # Given
        n = 10
        solution = Solution()

        # When
        actual = solution.tribonacci(n)

        # Then
        expected = 149
        self.assertEqual(actual, expected)
