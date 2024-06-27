"""
unit tests
"""

from unittest import TestCase
from algorithms.counters.group_anagrams.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_multiple_string_groups(self):
        # Given
        strings = ["apple", "banana", "window", "orange",
                   "pillow", "chair", "ocean", "garden"]
        solution = Solution()

        # When
        groups = solution.group_anagrams(strings)
        actual = {frozenset(group) for group in groups}

        # Then
        expected = {frozenset({"apple"}), frozenset({"banana"}), frozenset({"window"}), frozenset({"orange"}),
                    frozenset({"pillow"}), frozenset({"chair"}), frozenset({"ocean"}), frozenset({"garden"})}
        self.assertEqual(actual, expected)

    def test_some_multiple_string_groups(self):
        # Given
        strings = ["apple", "banana", "window", "orange",
                   "pillow", "chair", "ocean", "garden",
                   "elppa", "wodniw", "wollip", "naeco"]
        solution = Solution()

        # When
        groups = solution.group_anagrams(strings)
        actual = {frozenset(group) for group in groups}

        # Then
        expected = {frozenset({"apple", "elppa"}), frozenset({"banana"}), frozenset({"window", "wodniw"}), frozenset({"orange"}),
                    frozenset({"pillow", "wollip"}), frozenset({"chair"}), frozenset({"ocean", "naeco"}), frozenset({"garden"})}
        self.assertEqual(actual, expected)
