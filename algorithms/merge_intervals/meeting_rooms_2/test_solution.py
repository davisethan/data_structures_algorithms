"""
unit tests
"""

from unittest import TestCase
from algorithms.merge_intervals.meeting_rooms_2.solution import Solution


class SolutionTestCase(TestCase):
    def test_sequential_tasks(self):
        # Given
        tasks = [(1, 3), (5, 7), (9, 11), (13, 15), (17, 19)]
        solution = Solution()

        # When
        actual = solution.find_rooms(tasks)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_nonsequential_tasks(self):
        # Given
        tasks = [(1, 3), (2, 4), (5, 7), (6, 8), (9, 11), (10, 12)]
        solution = Solution()

        # When
        actual = solution.find_rooms(tasks)

        # Then
        expected = 2
        self.assertEqual(actual, expected)
