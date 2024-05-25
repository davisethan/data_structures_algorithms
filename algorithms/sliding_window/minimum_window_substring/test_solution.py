"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.minimum_window_substring.solution import Solution


class SolutionTestCase(TestCase):
    def test_shorter_first_string(self):
        # Given
        string1 = "azxeytjmnkwhzbdloifg"
        string2 = "azxeytjmnkwhzbdloifgazxeytjmnkwhzbdloifg"
        solution = Solution()

        # When
        actual = solution.minimum_window_substring(string1, string2)

        # Then
        expected = str()
        self.assertEqual(actual, expected)

    def test_zero_matches(self):
        # Given
        string1 = "azxeytjmnkwhzbdloifg"
        string2 = "aaaaaaaaaaaaaaaaaaaa"
        solution = Solution()

        # When
        actual = solution.minimum_window_substring(string1, string2)

        # Then
        expected = str()
        self.assertEqual(actual, expected)

    def test_one_match(self):
        # Given
        string1 = "azxeytpzqrwhzbdloifg"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_substring(string1, string2)

        # Then
        expected = "pzqr"
        self.assertEqual(actual, expected)

    def test_two_matches_return_frist(self):
        # Given
        string1 = "azpzqrjmnkwhzpzqrifg"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_substring(string1, string2)

        # Then
        expected = "pzqr"
        self.assertEqual(actual, expected)

    def test_two_matches_return_second(self):
        # Given
        string1 = "apzqrtjmnkwhzbpqrifg"
        string2 = "pqr"
        solution = Solution()

        # When
        actual = solution.minimum_window_substring(string1, string2)

        # Then
        expected = "pqr"
        self.assertEqual(actual, expected)

    def test_worst_case(self):
        # Given
        string1 = "aaaaaaaaaaaaaaaaaaaz"
        string2 = "z"
        solution = Solution()

        # When
        actual = solution.minimum_window_substring(string1, string2)

        # Then
        expected = "z"
        self.assertEqual(actual, expected)
