"""
unit tests
"""

from unittest import TestCase
from algorithms.backtracking.n_queens.solution import Solution


class SolutionTestCase(TestCase):
    def test_one_by_one_chessboard(self):
        # Given
        n = 1
        solution = Solution()

        # When
        actual = solution.solve_n_queens(n)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_four_by_four_chessboard(self):
        # Given
        n = 4
        solution = Solution()

        # When
        actual = solution.solve_n_queens(n)

        # Then
        expected = 2
        self.assertEqual(actual, expected)

    def test_six_by_six_chessboard(self):
        # Given
        n = 6
        solution = Solution()

        # When
        actual = solution.solve_n_queens(n)

        # Then
        expected = 4
        self.assertEqual(actual, expected)
