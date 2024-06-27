"""
unit tests
"""

from unittest import TestCase
from algorithms.counters.ransom_note.solution import Solution


class SolutionTestCase(TestCase):
    def test_character_mismatch(self):
        # Given
        note = "meetinthealley"
        magazine = "meetinthealle"
        solution = Solution()

        # When
        actual = solution.can_construct(note, magazine)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_character_frequency_mismatch(self):
        # Given
        note = "meetinthealley"
        magazine = "metinthealley"
        solution = Solution()

        # When
        actual = solution.can_construct(note, magazine)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_ransom_note_construction_succeeds(self):
        # Given
        note = "meetinthealley"
        magazine = "meetinthealley"
        solution = Solution()

        # When
        actual = solution.can_construct(note, magazine)

        # Then
        expected = True
        self.assertEqual(actual, expected)
