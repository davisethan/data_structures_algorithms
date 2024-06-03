"""
unit tests
"""

from unittest import TestCase
from algorithms.top_k_elements.k_closest_points_to_origin.solution import Solution, Point


class SolutionTestCase(TestCase):
    def test_points_on_unit_square(self):
        # Given
        points = [Point(1, 0), Point(1, 1), Point(0, 1), Point(-1, 1),
                  Point(-1, 0), Point(-1, -1), Point(0, -1), Point(1, -1)]
        k = 4
        solution = Solution()

        # When
        closest = solution.k_closest(points, k)
        actual = set(closest)

        # Then
        expected = set([(1, 0), (0, 1), (-1, 0), (0, -1)])
        self.assertEqual(actual, expected)

    def test_points_on_unit_square_plus_origin(self):
        # Given
        points = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1), Point(-1, 1),
                  Point(-1, 0), Point(-1, -1), Point(0, -1), Point(1, -1)]
        k = 4
        solution = Solution()

        # When
        closest = solution.k_closest(points, k)
        actual = set(closest)

        # Then
        expected = set([(0, 0), (1, 0), (0, 1), (0, -1)])
        self.assertEqual(actual, expected)
