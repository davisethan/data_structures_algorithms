"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.house_robber_2.solution import Solution


class SolutionTestCase(TestCase):
    def test_one_house(self):
        # Given
        money = [33]
        solution = Solution()

        # When
        actual = solution.house_robber(money)

        # Then
        expected = 33
        self.assertEqual(actual, expected)

    def test_first_house_included(self):
        # Given
        money = [38, 11, 17, 35, 33, 15, 32, 31, 18]
        solution = Solution()

        # When
        actual = solution.house_robber(money)

        # Then
        expected = 120
        self.assertEqual(actual, expected)

    def test_first_house_excluded(self):
        # Given
        money = [11, 38, 17, 35, 33, 15, 32, 31, 12]
        solution = Solution()

        # When
        actual = solution.house_robber(money)

        # Then
        expected = 119
        self.assertEqual(actual, expected)

    def test_last_house_included(self):
        # Given
        money = [17, 35, 33, 15, 32, 31, 19, 12, 38]
        solution = Solution()

        # When
        actual = solution.house_robber(money)

        # Then
        expected = 124
        self.assertEqual(actual, expected)

    def test_last_house_excluded(self):
        # Given
        money = [17, 37, 33, 15, 32, 31, 11, 39, 12]
        solution = Solution()

        # When
        actual = solution.house_robber(money)

        # Then
        expected = 122
        self.assertEqual(actual, expected)
