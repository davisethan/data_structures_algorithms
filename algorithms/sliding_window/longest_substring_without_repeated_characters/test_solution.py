"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.longest_substring_without_repeated_characters.solution import Solution


class SolutionTestCase(TestCase):
    def test_longest_window_without_repeats(self):
        # Given
        string = "abcdefgh"
        solution = Solution()

        # When
        actual = solution.find_longest_substring(string)

        # Then
        expected = 8
        self.assertEqual(actual, expected)

    def test_longest_window_before_repeats(self):
        # Given
        string = "abcdefghijkzpqrzabcdefgh"
        solution = Solution()

        # When
        actual = solution.find_longest_substring(string)

        # Then
        expected = 15
        self.assertEqual(actual, expected)

    def test_longest_window_after_repeats(self):
        # Given
        string = "abcdefghzpqrzabcdefghijk"
        solution = Solution()

        # When
        actual = solution.find_longest_substring(string)

        # Then
        expected = 15
        self.assertEqual(actual, expected)

    def test_worst_case_window_length_one(self):
        # Given
        string = "aaaaaaaaaa"
        solution = Solution()

        # When
        actual = solution.find_longest_substring(string)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_worst_case_window_length_string_length(self):
        # Given
        string = "abcdefgha"
        solution = Solution()

        # When
        actual = solution.find_longest_substring(string)

        # Then
        expected = 8
        self.assertEqual(actual, expected)
