"""
unit tests
"""

from unittest import TestCase
from algorithms.merge_intervals.intervals_intersection.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_intersections(self):
        # Given
        intervals1 = [[1, 3], [7, 9], [13, 15]]
        intervals2 = [[4, 6], [10, 12], [16, 18]]
        solution = Solution()

        # When
        actual = solution.intervals_intersection(intervals1, intervals2)

        # Then
        expected = []
        self.assertEqual(actual, expected)

    def test_some_intersections(self):
        # Given
        intervals1 = [[1, 3], [5, 10], [11, 12]]
        intervals2 = [[2, 4], [6, 9], [11, 12]]
        solution = Solution()

        # When
        actual = solution.intervals_intersection(intervals1, intervals2)

        # Then
        expected = [[2, 3], [6, 9], [11, 12]]
        self.assertEqual(actual, expected)
