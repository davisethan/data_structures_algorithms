"""
unit tests
"""

from unittest import TestCase
from algorithms.greedy_techniques.two_city_scheduling.solution import Solution


class SolutionTestCase(TestCase):
    def test_a_strictly_less_than_b(self):
        # Given
        costs = [[45, 135], [80, 200], [115, 265], [150, 330],
                 [185, 395], [220, 460], [255, 525], [290, 590]]
        solution = Solution()

        # When
        actual = solution.two_city_scheduling(costs)

        # Then
        expected = 1880
        self.assertEqual(actual, expected)

    def test_a_strictly_greater_than_b(self):
        # Given
        costs = [[135, 45], [200, 80], [265, 115], [330, 150],
                 [395, 185], [460, 220], [525, 255], [590, 290]]
        solution = Solution()

        # When
        actual = solution.two_city_scheduling(costs)

        # Then
        expected = 1880
        self.assertEqual(actual, expected)

    def test_a_less_than_b_intersects(self):
        # Given
        costs = [[45, 135], [110, 170], [175, 205], [240, 240],
                 [305, 275], [370, 310], [435, 345], [500, 380]]
        solution = Solution()

        # When
        actual = solution.two_city_scheduling(costs)

        # Then
        expected = 1880
        self.assertEqual(actual, expected)

    def test_a_greater_than_b_intersects(self):
        # Given
        costs = [[135, 45], [170, 110], [205, 175], [240, 240],
                 [275, 305], [310, 370], [345, 435], [380, 500]]
        solution = Solution()

        # When
        actual = solution.two_city_scheduling(costs)

        # Then
        expected = 1880
        self.assertEqual(actual, expected)
