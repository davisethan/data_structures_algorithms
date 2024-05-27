"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.find_repeated_sequences.solution import Solution


class SolutionTestCase(TestCase):
    def test_empty_string(self):
        # Given
        string = str()
        length = 5
        solution = Solution()

        # When
        actual = solution.find_repeated_sequences(string, length)

        # Then
        expected = set()
        self.assertEqual(actual, expected)

    def test_zero_repeats(self):
        # Given
        string = "ACGTGACGTACGTTGCACTG"
        length = 5
        solution = Solution()

        # When
        actual = solution.find_repeated_sequences(string, length)

        # Then
        expected = set()
        self.assertEqual(actual, expected)

    def test_all_repeats(self):
        # Given
        string = "AAAAAAAAAAAAAAAAAAAA"
        length = 5
        solution = Solution()

        # When
        actual = solution.find_repeated_sequences(string, length)

        # Then
        expected = {"AAAAA"}
        self.assertEqual(actual, expected)

    def test_some_repeats(self):
        # Given
        string = "ACGTTACGACGTTACGACGT"
        length = 5
        solution = Solution()

        # When
        actual = solution.find_repeated_sequences(string, length)

        # Then
        expected = {"ACGTT", "CGTTA", "GTTAC", "TTACG",
                    "TACGA", "ACGAC", "CGACG", "GACGT"}
        self.assertEqual(actual, expected)
