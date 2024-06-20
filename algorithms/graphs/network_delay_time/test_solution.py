"""
unit tests
"""

from unittest import TestCase
from algorithms.graphs.network_delay_time.solution import Solution


class SolutionTestCase(TestCase):
    def test_existent_solution(self):
        # Given
        times = [(0, 1, 18), (0, 2, 16), (1, 2, 4), (1, 3, 1), (1, 4, 10),
                 (2, 3, 13), (2, 4, 14), (3, 4, 20), (3, 5, 15), (3, 4, 20), (4, 5, 19)]
        n = 6
        k = 0
        solution = Solution()

        # When
        actual = solution.network_delay_time(times, n, k)

        # Then
        expected = 34
        self.assertEqual(actual, expected)

    def test_nonexistent_solution(self):
        # Given
        times = [(0, 1, 18), (0, 2, 16), (1, 2, 4),
                 (3, 4, 20), (3, 5, 15), (4, 5, 19)]
        n = 6
        k = 0
        solution = Solution()

        # When
        actual = solution.network_delay_time(times, n, k)

        # Then
        expected = -1
        self.assertEqual(actual, expected)
