"""
unit tests
"""

from unittest import TestCase
from algorithms.matrices.rotate_image.solution import Solution


class SolutionTestCase(TestCase):
    def test_three_by_three_matrix(self):
        # Given
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        solution = Solution()

        # When
        actual = solution.rotate_image(matrix)

        # Then
        expected = [[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]
        self.assertEqual(actual, expected)

    def test_four_by_four_matrix(self):
        # Given
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]
        solution = Solution()

        # When
        actual = solution.rotate_image(matrix)

        # Then
        expected = [[13, 9, 5, 1],
                    [14, 10, 6, 2],
                    [15, 11, 7, 3],
                    [16, 12, 8, 4]]
        self.assertEqual(actual, expected)
