"""
unit tests
"""

from unittest import TestCase
from algorithms.union_find.redundant_connection.solution import Solution


class SolutionTestCase(TestCase):
    def test_all_paths_cyclic(self):
        # Given
        edges = [(0, 1), (1, 2), (2, 3), (3, 4),
                 (4, 5), (5, 6), (6, 7), (7, 0)]
        solution = Solution()

        # When
        actual = solution.redundant_connection(edges)

        # Then
        expected = [7, 0]
        self.assertEqual(actual, expected)

    def test_some_paths_cyclic(self):
        # Given
        edges = [(1, 2), (1, 3), (2, 4), (2, 5),
                 (3, 6), (3, 7), (4, 8), (7, 8)]
        solution = Solution()

        # When
        actual = solution.redundant_connection(edges)

        # Then
        expected = [7, 8]
        self.assertEqual(actual, expected)
