"""
unit tests
"""

from unittest import TestCase
from algorithms.topological_sort.course_schedule.solution import Solution


class SolutionTestCase(TestCase):
    def test_all_courses_can_be_taken(self):
        # Given
        n = 6
        prerequisites = [(2, 0), (2, 1), (3, 0), (3, 1), (4, 3), (5, 2)]
        solution = Solution()

        # When
        actual = solution.can_finish(n, prerequisites)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_not_all_courses_can_be_taken(self):
        # Given
        n = 2
        prerequisites = [(1, 0), (0, 1)]
        solution = Solution()

        # When
        actual = solution.can_finish(n, prerequisites)

        # Then
        expected = False
        self.assertEqual(actual, expected)
