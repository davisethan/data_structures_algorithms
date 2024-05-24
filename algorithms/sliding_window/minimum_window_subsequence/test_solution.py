"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.minimum_window_subsequence.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_matches(self):
        # Given
        string1 = "hzcxyvksqwmfzjpturlo"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_subsequence(string1, string2)

        # Then
        expected = str()
        self.assertEqual(actual, expected)

    def test_one_match(self):
        # Given
        string1 = "hzcpyqrsqwmfzjpturlo"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_subsequence(string1, string2)

        # Then
        expected = "pyqr"
        self.assertEqual(actual, expected)

    def test_two_matches_return_first(self):
        # Given
        string1 = "hzcpyqrsqwmfzjptqrlo"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_subsequence(string1, string2)

        # Then
        expected = "pyqr"
        self.assertEqual(actual, expected)

    def test_two_matches_return_second(self):
        # Given
        string1 = "hzcpyqrsqwmfzjtpqrlo"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_subsequence(string1, string2)

        # Then
        expected = "pqr"
        self.assertEqual(actual, expected)

    def test_two_matches_overlap(self):
        # Given
        string1 = "hzcppqrsqwmfzjpturlo"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_subsequence(string1, string2)

        # Then
        expected = "pqr"
        self.assertEqual(actual, expected)

    def test_worst_case(self):
        # Given
        string1 = "aaaaaaaaaaaaaaaaaaaa"
        string2 = "aaa"
        solution = Solution()

        # When
        actual = solution.minimum_window_subsequence(string1, string2)

        # Then
        expected = "aaa"
        self.assertEqual(actual, expected)
