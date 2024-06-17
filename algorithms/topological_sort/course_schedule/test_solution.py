"""
unit tests
"""

from unittest import TestCase
from algorithms.topological_sort.course_schedule.solution import Solution


class SolutionTestCase(TestCase):
    def test_all_courses_in_prerequisites(self):
        # Given
        n = 6
        prerequisites = [(2, 0), (2, 1), (3, 0), (3, 1), (4, 3), (5, 2)]
        solution = Solution()

        # When
        actual = solution.find_order(n, prerequisites)

        # Then
        expected = [0, 1, 2, 3, 5, 4]
        self.assertEqual(actual, expected)

    def test_not_all_courses_in_prerequisites(self):
        # Given
        n = 7
        prerequisites = [(2, 0), (2, 1), (3, 0), (3, 1), (4, 3), (5, 2)]
        solution = Solution()

        # When
        actual = solution.find_order(n, prerequisites)

        # Then
        expected = [0, 1, 6, 2, 3, 5, 4]
        self.assertEqual(actual, expected)
