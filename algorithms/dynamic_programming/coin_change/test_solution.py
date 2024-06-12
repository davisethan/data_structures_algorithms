"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.coin_change.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_solution(self):
        # Given
        coins = [2, 3, 4, 5, 6, 7, 8, 10]
        total = 0
        solution = Solution()

        # When
        actual = solution.coin_change(coins, total)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_nonexistent_solution(self):
        # Given
        coins = [2, 3, 4, 5, 6, 7, 8, 10]
        total = 1
        solution = Solution()

        # When
        actual = solution.coin_change(coins, total)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_existent_solution(self):
        # Given
        coins = [2, 3, 4, 5, 6, 7, 8, 10]
        total = 32
        solution = Solution()

        # When
        actual = solution.coin_change(coins, total)

        # Then
        expected = 4
        self.assertEqual(actual, expected)
