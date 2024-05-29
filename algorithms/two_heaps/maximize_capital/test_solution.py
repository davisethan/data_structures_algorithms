"""
unit tests
"""

from unittest import TestCase
from algorithms.two_heaps.maximize_capital.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_capital(self):
        # Given
        c = 0
        k = 25
        capitals = [25, 35, 45, 55, 65]
        profits = [125, 135, 145, 155, 165]
        solution = Solution()

        # When
        actual = solution.maximum_capital(c, k, capitals, profits)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_cumulative_capital_less_than_all_project_capitals(self):
        # Given
        c = 10
        k = 25
        capitals = [25, 35, 45, 55, 65]
        profits = [125, 135, 145, 155, 165]
        solution = Solution()

        # When
        actual = solution.maximum_capital(c, k, capitals, profits)

        # Then
        expected = 10
        self.assertEqual(actual, expected)

    def test_cumulative_capital_less_than_some_project_capitals(self):
        # Given
        c = 10
        k = 25
        capitals = [5, 115, 335, 445, 555, 665]
        profits = [105, 215, 435, 545, 655, 765]
        solution = Solution()

        # When
        actual = solution.maximum_capital(c, k, capitals, profits)

        # Then
        expected = 330
        self.assertEqual(actual, expected)

    def test_cumulative_capital_greater_than_all_project_capitals(self):
        # Given
        c = 105
        k = 25
        capitals = [15, 25, 35, 45, 55]
        profits = [75, 85, 95, 105, 115]
        solution = Solution()

        # When
        actual = solution.maximum_capital(c, k, capitals, profits)

        # Then
        expected = 580
        self.assertEqual(actual, expected)

    def test_cumulative_capital_bound_by_maximum_number_of_projects(self):
        # Given
        c = 105
        k = 3
        capitals = [15, 25, 35, 45, 55]
        profits = [75, 85, 95, 105, 115]
        solution = Solution()

        # When
        actual = solution.maximum_capital(c, k, capitals, profits)

        # Then
        expected = 420
        self.assertEqual(actual, expected)
