"""
unit tests
"""

from unittest import TestCase
from algorithms.backtracking.sudoku_solver.solution import Solution


class SolutionTestCase(TestCase):
    def test_sudoku_solver(self):
        # Given
        board = [[".", ".", ".", ".", ".", ".", ".", "7", "."],
                 ["2", "7", "5", ".", ".", ".", "3", "1", "4"],
                 [".", ".", ".", ".", "2", "7", ".", "5", "."],
                 ["9", "8", ".", ".", ".", ".", ".", "3", "1"],
                 [".", "3", "1", "8", ".", "4", ".", ".", "."],
                 [".", ".", ".", "1", ".", ".", "8", ".", "5"],
                 ["7", ".", "6", "2", ".", ".", "1", "8", "."],
                 [".", "9", ".", "7", ".", ".", ".", ".", "."],
                 ["4", "1", ".", ".", ".", "5", ".", ".", "7"]]
        solution = Solution()

        # When
        actual = solution.solve_sudoku(board)

        # Then
        expected = [["8", "6", "3", "4", "5", "1", "2", "7", "9"],
                    ["2", "7", "5", "9", "8", "6", "3", "1", "4"],
                    ["1", "4", "9", "3", "2", "7", "6", "5", "8"],
                    ["9", "8", "7", "5", "6", "2", "4", "3", "1"],
                    ["5", "3", "1", "8", "9", "4", "7", "6", "2"],
                    ["6", "2", "4", "1", "7", "3", "8", "9", "5"],
                    ["7", "5", "6", "2", "4", "9", "1", "8", "3"],
                    ["3", "9", "2", "7", "1", "8", "5", "4", "6"],
                    ["4", "1", "8", "6", "3", "5", "9", "2", "7"]]
        self.assertEqual(actual, expected)
