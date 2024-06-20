"""
unit tests
"""

from unittest import TestCase
from algorithms.graphs.graph_valid_tree.solution import Solution


class SolutionTestCase(TestCase):
    def test_not_connected(self):
        # Given
        n = 7
        edges = [(0, 1), (1, 3), (1, 4), (2, 5), (2, 6)]
        solution = Solution()

        # When
        actual = solution.valid_tree(n, edges)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_cycle(self):
        # Given
        n = 7
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (1, 2),
                 (2, 5), (2, 6), (3, 4), (4, 5), (5, 6)]
        solution = Solution()

        # When
        actual = solution.valid_tree(n, edges)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_connected_and_no_cycle(self):
        # Given
        n = 7
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
        solution = Solution()

        # When
        actual = solution.valid_tree(n, edges)

        # Then
        expected = True
        self.assertEqual(actual, expected)
