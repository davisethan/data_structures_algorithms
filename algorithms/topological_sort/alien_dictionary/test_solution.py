"""
unit tests
"""

from unittest import TestCase
from algorithms.topological_sort.alien_dictionary.solution import Solution


class SolutionTestCase(TestCase):
    def test_nonexistent_edges(self):
        # Given
        words = ["pxlfajqn"]
        solution = Solution()

        # When
        actual = solution.alien_order(words)

        # Then
        expected = "pxlfajqn"
        self.assertEqual(actual, expected)

    def test_existent_edges(self):
        # Given
        words = ["pxlfajqn", "hrkbtsvm", "wygduzen", "qcpxjoal"]
        solution = Solution()

        # When
        actual = solution.alien_order(words)

        # Then
        expected = "pxlfajnrkbtsvmygduzecohwq"
        self.assertEqual(actual, expected)

    def test_graph_cycle(self):
        # Given
        words = ["pxlfajqn", "hrkbtsvm", "wygduzen", "pcpxjoal"]
        solution = Solution()

        # When
        actual = solution.alien_order(words)

        # Then
        expected = ""
        self.assertEqual(actual, expected)

    def test_character_less_than_whitespace_contradiction(self):
        # Given
        words = ["pxlfajqn", "pxlfa"]
        solution = Solution()

        # When
        actual = solution.alien_order(words)

        # Then
        expected = ""
        self.assertEqual(actual, expected)
