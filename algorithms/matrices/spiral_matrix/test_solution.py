"""
unit tests
"""

from unittest import TestCase
from algorithms.matrices.spiral_matrix.solution import Solution


class SolutionTestCase(TestCase):
    def test_three_by_three_matrix(self):
        # Given
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        solution = Solution()

        # When
        actual = solution.spiral_order(matrix)

        # Then
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(actual, expected)

    def test_four_by_four_matrix(self):
        # Given
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]
        solution = Solution()

        # When
        actual = solution.spiral_order(matrix)

        # Then
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(actual, expected)
