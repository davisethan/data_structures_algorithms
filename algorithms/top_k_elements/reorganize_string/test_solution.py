"""
unit tests
"""

from unittest import TestCase
from algorithms.top_k_elements.reorganize_string.solution import Solution


class SolutionTestCase(TestCase):
    def test_not_enough_unique_characters(self):
        # Given
        string = "aaaaaxyz"
        solution = Solution()

        # When
        actual = solution.reorganize_string(string)

        # Then
        expected = str()
        self.assertEqual(actual, expected)

    def test_just_enough_unique_characters(self):
        # Given
        string = "aaaaawxyz"
        solution = Solution()

        # When
        actual = solution.reorganize_string(string)

        # Then
        expected = "awaxayaza"
        self.assertEqual(actual, expected)

    def test_more_than_enough_unique_characters(self):
        # Given
        string = "aaaaauvwxyz"
        solution = Solution()

        # When
        actual = solution.reorganize_string(string)

        # Then
        expected = "auavawaxayz"
        self.assertEqual(actual, expected)
