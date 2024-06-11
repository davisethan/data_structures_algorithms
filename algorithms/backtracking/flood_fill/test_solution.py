"""
unit tests
"""

from unittest import TestCase
from algorithms.backtracking.flood_fill.solution import Solution


class SolutionTestCase(TestCase):
    def test_source_at_target_level(self):
        # Given
        grid = [[3, 7, 1, 8, 4],
                [5, 2, 6, 1, 7],
                [4, 8, 3, 5, 2],
                [6, 1, 7, 3, 8],
                [2, 4, 5, 6, 1]]
        sr, sc = 2, 3
        target = 5
        solution = Solution()

        # When
        actual = solution.flood_fill(grid, sr, sc, target)

        # Then
        expected = [[3, 7, 1, 8, 4],
                    [5, 2, 6, 1, 7],
                    [4, 8, 3, 5, 2],
                    [6, 1, 7, 3, 8],
                    [2, 4, 5, 6, 1]]
        self.assertEqual(actual, expected)

    def test_source_not_at_target_level(self):
        # Given
        grid = [[3, 7, 3, 3, 3],
                [5, 3, 6, 3, 3],
                [4, 8, 3, 3, 2],
                [6, 1, 7, 3, 8],
                [3, 3, 3, 3, 1]]
        sr, sc = 2, 3
        target = 5
        solution = Solution()

        # When
        actual = solution.flood_fill(grid, sr, sc, target)

        # Then
        expected = [[3, 7, 5, 5, 5],
                    [5, 3, 6, 5, 5],
                    [4, 8, 5, 5, 2],
                    [6, 1, 7, 5, 8],
                    [5, 5, 5, 5, 1]]
        self.assertEqual(actual, expected)
