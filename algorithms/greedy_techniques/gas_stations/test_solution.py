"""
unit tests
"""

from unittest import TestCase
from algorithms.greedy_techniques.gas_stations.solution import Solution


class SolutionTestCase(TestCase):
    def test_no_solution(self):
        # Given
        gas = [1, 2, 3, 4, 5]
        cost = [6, 5, 4, 3, 2]
        solution = Solution()

        # When
        actual = solution.journey(gas, cost)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_starting_index_at_start_of_array(self):
        # Given
        gas = [5, 4, 3, 2, 1]
        cost = [1, 2, 3, 4, 5]
        solution = Solution()

        # When
        actual = solution.journey(gas, cost)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_starting_index_in_middle_of_array(self):
        # Given
        gas = [1, 2, 5, 4, 3]
        cost = [4, 5, 1, 2, 3]
        solution = Solution()

        # When
        actual = solution.journey(gas, cost)

        # Then
        expected = 2
        self.assertEqual(actual, expected)

    def test_starting_index_at_end_of_array(self):
        # Given
        gas = [5, 3, 7, 11]
        cost = [7, 1, 11, 7]
        solution = Solution()

        # When
        actual = solution.journey(gas, cost)

        # Then
        expected = 3
        self.assertEqual(actual, expected)
