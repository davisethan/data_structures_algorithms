"""
unit tests
"""

from unittest import TestCase
from algorithms.union_find.number_of_islands.solution import Solution


class SolutionTestCase(TestCase):
    def test_number_of_islands(self):
        # Given
        grid = [[1, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 1],
                [1, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 1, 1],
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 1]]
        solution = Solution()

        # When
        actual = solution.number_of_islands(grid)

        # Then
        expected = 5
        self.assertEqual(actual, expected)
