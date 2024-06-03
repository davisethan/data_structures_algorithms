"""
unit tests
"""

from unittest import TestCase
from algorithms.top_k_elements.top_k_frequent_words.solution import Solution


class SolutionTestCase(TestCase):
    def test_no_duplicate_frequencies(self):
        # Given
        words = ["example",
                 "harmony", "harmony",
                 "freedom", "freedom", "freedom",
                 "journey", "journey", "journey", "journey",
                 "tranquil", "tranquil", "tranquil", "tranquil", "tranquil",
                 "library", "library", "library", "library", "library", "library",
                 "sunshine", "sunshine", "sunshine", "sunshine", "sunshine", "sunshine", "sunshine",
                 "blossom", "blossom", "blossom", "blossom", "blossom", "blossom", "blossom", "blossom",
                 "adventure", "adventure", "adventure", "adventure", "adventure", "adventure", "adventure", "adventure", "adventure"]
        k = 3
        solution = Solution()

        # When
        actual = solution.top_k_frequent(words, k)

        # Then
        expected = ["adventure", "blossom", "sunshine"]
        self.assertEqual(actual, expected)

    def test_some_duplicate_frequencies(self):
        # Given
        words = ["example",
                 "harmony", "harmony", "harmony",
                 "freedom", "freedom", "freedom",
                 "journey", "journey", "journey", "journey", "journey", "journey",
                 "tranquil", "tranquil", "tranquil", "tranquil", "tranquil", "tranquil",
                 "library", "library", "library", "library", "library", "library",
                 "sunshine", "sunshine", "sunshine", "sunshine", "sunshine", "sunshine", "sunshine", "sunshine", "sunshine",
                 "blossom", "blossom", "blossom", "blossom", "blossom", "blossom", "blossom", "blossom", "blossom",
                 "adventure", "adventure", "adventure", "adventure", "adventure", "adventure", "adventure", "adventure", "adventure"]
        k = 3
        solution = Solution()

        # When
        actual = solution.top_k_frequent(words, k)

        # Then
        expected = ["adventure", "blossom", "sunshine"]
        self.assertEqual(actual, expected)
