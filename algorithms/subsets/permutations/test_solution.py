"""
unit tests
"""

from unittest import TestCase
from algorithms.subsets.permutations.solution import Solution


class SolutionTestCase(TestCase):
    def test_single_character_word(self):
        # Given
        word = "d"
        solution = Solution()

        # When
        actual = solution.find_permutations(word)

        # Then
        expected = ["d"]
        self.assertEqual(actual, expected)

    def test_multi_character_word(self):
        # Given
        word = "dog"
        solution = Solution()

        # When
        actual = solution.find_permutations(word)

        # Then
        expected = ["dog", "dgo", "odg", "ogd", "gdo", "god"]
        self.assertEqual(actual, expected)
