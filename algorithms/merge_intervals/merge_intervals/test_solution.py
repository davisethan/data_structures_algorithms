"""
unit tests
"""

from unittest import TestCase
from algorithms.merge_intervals.merge_intervals.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_overlapping_intervals(self):
        # Given
        intervals = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15]]
        solution = Solution()

        # When
        actual = solution.merge_intervals(intervals)

        # Then
        expected = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15]]
        self.assertEqual(actual, expected)

    def test_some_overlapping_intervals(self):
        # Given
        intervals = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 11], [10, 12]]
        solution = Solution()

        # When
        actual = solution.merge_intervals(intervals)

        # Then
        expected = [[1, 4], [5, 8], [9, 12]]
        self.assertEqual(actual, expected)

    def test_all_overlapping_intervals(self):
        # Given
        intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]
        solution = Solution()

        # When
        actual = solution.merge_intervals(intervals)

        # Then
        expected = [[1, 7]]
        self.assertEqual(actual, expected)
