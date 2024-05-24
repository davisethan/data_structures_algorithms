"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.longest_repeated_character_replacement.solution import Solution


class SolutionTestCase(TestCase):
    def test_longest_repeated_contiguous_at_start(self):
        # Given
        string = "aaaaaaaaaaxerkjysuhf"
        capacity = 2
        solution = Solution()

        # When
        actual = solution.longest_repeated_character_replacement(
            string, capacity)

        # Then
        expected = 12
        self.assertEqual(actual, expected)

    def test_longest_repeated_contiguous_at_middle(self):
        # Given
        string = "wzomqaaaaaaaaaaysuhf"
        capacity = 2
        solution = Solution()

        # When
        actual = solution.longest_repeated_character_replacement(
            string, capacity)

        # Then
        expected = 12
        self.assertEqual(actual, expected)

    def test_longest_repeated_contiguous_at_end(self):
        # Given
        string = "wzomqvtnlbaaaaaaaaaa"
        capacity = 2
        solution = Solution()

        # When
        actual = solution.longest_repeated_character_replacement(
            string, capacity)

        # Then
        expected = 12
        self.assertEqual(actual, expected)

    def test_longest_repeated_noncontiguous_at_start(self):
        # Given
        string = "aaaaavaaaaaerkjysuhf"
        capacity = 2
        solution = Solution()

        # When
        actual = solution.longest_repeated_character_replacement(
            string, capacity)

        # Then
        expected = 12
        self.assertEqual(actual, expected)

    def test_longest_repeated_noncontiguous_at_middle(self):
        # Given
        string = "wzoaaaaalbaaaaaysuhf"
        capacity = 2
        solution = Solution()

        # When
        actual = solution.longest_repeated_character_replacement(
            string, capacity)

        # Then
        expected = 12
        self.assertEqual(actual, expected)

    def test_longest_repeated_noncontiguous_at_end(self):
        # Given
        string = "wzomqvtnlaaaaajaaaaa"
        capacity = 2
        solution = Solution()

        # When
        actual = solution.longest_repeated_character_replacement(
            string, capacity)

        # Then
        expected = 12
        self.assertEqual(actual, expected)
