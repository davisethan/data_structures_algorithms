"""
unit tests
"""

from unittest import TestCase
from algorithms.backtracking.word_search.solution import Solution


class SolutionTestCase(TestCase):
    def test_no_solution(self):
        # Given
        grid = [["g", "e", "n", "m", "q"],
                ["t", "y", "l", "r", "b"],
                ["k", "x", "p", "u", "z"],
                ["a", "f", "h", "j", "s"]]
        word = "snakesandsnakes"
        solution = Solution()

        # When
        actual = solution.word_search(grid, word)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_some_solution(self):
        # Given
        grid = [["g", "d", "n", "e", "k"],
                ["s", "s", "a", "s", "a"],
                ["e", "n", "p", "u", "n"],
                ["k", "a", "h", "j", "s"]]
        word = "snakesandsnakes"
        solution = Solution()

        # When
        actual = solution.word_search(grid, word)

        # Then
        expected = True
        self.assertEqual(actual, expected)
