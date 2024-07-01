"""
unit tests
"""

from unittest import TestCase
from algorithms.union_find.regions_cut_by_slashes.solution import Solution


class SolutionTestCase(TestCase):
    def test_regions_cut_by_slashes(self):
        # Given
        grid = [" /\\ ", "//\\\\", "\\\\//", " \\/ "]
        solution = Solution()

        # When
        actual = solution.regions_cut_by_slashes(grid)

        # Then
        expected = 6
        self.assertEqual(actual, expected)
