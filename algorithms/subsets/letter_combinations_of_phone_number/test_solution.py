"""
unit tests
"""

from unittest import TestCase
from algorithms.subsets.letter_combinations_of_phone_number.solution import Solution


class SolutionTestCase(TestCase):
    def test_empty_digits(self):
        # Given
        digits = ""
        solution = Solution()

        # When
        actual = solution.letter_combinations(digits)

        # Then
        expected = []
        self.assertEqual(actual, expected)

    def test_mixed_digits(self):
        # Given
        digits = "357"
        solution = Solution()

        # When
        actual = solution.letter_combinations(digits)

        # Then
        expected = ["djp", "djq", "djr", "djs",
                    "dkp", "dkq", "dkr", "dks",
                    "dlp", "dlq", "dlr", "dls",
                    "ejp", "ejq", "ejr", "ejs",
                    "ekp", "ekq", "ekr", "eks",
                    "elp", "elq", "elr", "els",
                    "fjp", "fjq", "fjr", "fjs",
                    "fkp", "fkq", "fkr", "fks",
                    "flp", "flq", "flr", "fls"]
        self.assertEqual(actual, expected)
