"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.word_break.solution import Solution


class SolutionTestCase(TestCase):
    def test_existent_solution(self):
        # Given
        string = "catsanddogsandbirds"
        dictionary = {"cats", "and", "sand", "dogs", "birds"}
        solution = Solution()

        # When
        actual = solution.word_break(string, dictionary)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_nonexistent_solution(self):
        # Given
        string = "catsandogsandbirds"
        dictionary = {"cats", "and", "sand", "dogs", "birds"}
        solution = Solution()

        # When
        actual = solution.word_break(string, dictionary)

        # Then
        expected = False
        self.assertEqual(actual, expected)
