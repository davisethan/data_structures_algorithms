"""
unit tests
"""

from unittest import TestCase
from algorithms.graphs.clone_graph.solution import Solution, Node


class SolutionTestCase(TestCase):
    def test_solution(self):
        # Given
        a, b, c, d = Node(0), Node(1), Node(2), Node(3)
        a.neighbors = [b, c, d]
        b.neighbors = [a, c]
        c.neighbors = [a, b, d]
        d.neighbors = [a, c]
        solution = Solution()

        # When
        a2 = solution.clone(a)
        b2, c2, d2 = a2.neighbors

        # Then
        self.assertEqual(a, a2)
        self.assertEqual(b, b2)
        self.assertEqual(c, c2)
        self.assertEqual(d, d2)
