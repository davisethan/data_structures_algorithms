"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.knapsack_01.solution import Solution


class SolutionTestCase(TestCase):
    def test_01_knapskack(self):
        # Given
        capacity = 150
        weights = [15, 26, 38, 49, 54, 68]
        values = [24, 37, 43, 58, 67, 74]
        solution = Solution()

        # When
        actual = solution.max_profit(capacity, weights, values)

        # Then
        expected = 186
        self.assertEqual(actual, expected)
