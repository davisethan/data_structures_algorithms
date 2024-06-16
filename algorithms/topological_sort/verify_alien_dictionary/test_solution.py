"""
unit tests
"""

from unittest import TestCase
from algorithms.topological_sort.verify_alien_dictionary.solution import Solution


class SolutionTestCase(TestCase):
    def test_words_not_in_order(self):
        # Given
        alphabet = "udlzgvqvcfmtwjsrpakxbynhio"
        words = ["umbrella", "whale", "queen",  "igloo", "apple"]
        solution = Solution()

        # When
        actual = solution.verify_alien_dictionary(words, alphabet)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_words_in_order(self):
        # Given
        alphabet = "udlzgvqvcfmtwjsrpakxbynhio"
        words = ["umbrella", "queen", "whale", "apple", "igloo"]
        solution = Solution()

        # When
        actual = solution.verify_alien_dictionary(words, alphabet)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_character_less_than_whitespace_contradiction(self):
        # Given
        alphabet = "udlzgvqvcfmtwjsrpakxbynhio"
        words = ["umbrellas", "umbrella", "zebras", "zebra"]
        solution = Solution()

        # When
        actual = solution.verify_alien_dictionary(words, alphabet)

        # Then
        expected = False
        self.assertEqual(actual, expected)
