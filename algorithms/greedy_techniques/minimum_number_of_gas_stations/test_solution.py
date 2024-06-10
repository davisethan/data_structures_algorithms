"""
unit tests
"""

from unittest import TestCase
from algorithms.greedy_techniques.minimum_number_of_gas_stations.solution import Solution


class SolutionTestCase(TestCase):
    def test_initial_fuel_greater_than_or_equal_to_target(self):
        # Given
        target = 27
        fuel = 30
        stations = [(3, 2), (5, 4), (9, 2), (11, 3),
                    (14, 4), (18, 4), (22, 5), (27, 0)]
        solution = Solution()

        # When
        actual = solution.minimum_refuel_stops(target, fuel, stations)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_unable_to_reach_fuel_station(self):
        # Given
        target = 27
        fuel = 3
        stations = [(3, 2), (5, 4), (9, 2), (11, 3),
                    (14, 4), (18, 3), (22, 5), (27, 0)]
        solution = Solution()

        # When
        actual = solution.minimum_refuel_stops(target, fuel, stations)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_unable_to_reach_target(self):
        # Given
        target = 27
        fuel = 3
        stations = [(3, 2), (5, 4), (9, 2), (11, 3),
                    (14, 4), (18, 4), (22, 4), (27, 0)]
        solution = Solution()

        # When
        actual = solution.minimum_refuel_stops(target, fuel, stations)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_able_to_reach_target(self):
        # Given
        target = 27
        fuel = 3
        stations = [(3, 2), (5, 4), (9, 2), (11, 3),
                    (14, 4), (18, 4), (22, 5), (27, 0)]
        solution = Solution()

        # When
        actual = solution.minimum_refuel_stops(target, fuel, stations)

        # Then
        expected = 7
        self.assertEqual(actual, expected)
