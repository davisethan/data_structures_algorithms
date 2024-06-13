"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.climbing_stairs.solution import Solution


class SolutionTestCase(TestCase):
    def test_one_step(self):
        # Given
        n = 1
        solution = Solution()

        # When
        actual = solution.climb_stairs(n)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_ten_steps(self):
        # Given
        n = 10
        solution = Solution()

        # When
        actual = solution.climb_stairs(n)

        # Then
        expected = 89
        self.assertEqual(actual, expected)
