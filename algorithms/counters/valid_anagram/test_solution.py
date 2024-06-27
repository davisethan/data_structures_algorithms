"""
unit tests
"""

from unittest import TestCase
from algorithms.counters.valid_anagram.solution import Solution


class SolutionTestCase(TestCase):
    def test_character_mismatch(self):
        # Given
        string1 = "xmtdkjswqblefinxgcvp"
        string2 = "ymtdkjswqblefinxgcvp"
        solution = Solution()

        # When
        actual = solution.is_anagram(string1, string2)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_character_frequency_mismatch(self):
        # Given
        string1 = "xmtdkjswqblefinxgcvp"
        string2 = "mmtdkjswqblefinxgcvp"
        solution = Solution()

        # When
        actual = solution.is_anagram(string1, string2)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_is_anagram_frequency(self):
        # Given
        string1 = "xmtdkjswqblefinxgcvp"
        string2 = "xmtdkjswqblefinxgcvp"
        solution = Solution()

        # When
        actual = solution.is_anagram(string1, string2)

        # Then
        expected = True
        self.assertEqual(actual, expected)
