"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.matrix_01.solution import Solution


class SolutionTestCase(TestCase):
    def test_distance(self):
        # Given
        matrix = [[1, 1, 1, 0, 1, 1],
                  [1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 0, 1],
                  [1, 0, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1]]
        solution = Solution()

        # When
        actual = solution.distance(matrix)

        # Then
        expected = [[3, 2, 1, 0, 1, 2],
                    [2, 1, 0, 1, 1, 2],
                    [2, 1, 1, 1, 0, 1],
                    [1, 0, 1, 2, 1, 1],
                    [1, 1, 2, 2, 1, 0],
                    [0, 1, 2, 3, 2, 1]]
        self.assertEqual(actual, expected)
