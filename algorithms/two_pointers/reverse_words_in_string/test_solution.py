"""
unit tests
"""

from unittest import TestCase
from algorithms.two_pointers.reverse_words_in_string.solution import Solution


class SolutionTestCase(TestCase):
    def test_reverse_words_in_string(self):
        # Given
        sentence = "  the  quick  brown  fox  jumps  over  the  lazy  dog  "
        solution = Solution()

        # When
        actual = solution.reverse_words(sentence)

        # Then
        expected = "dog lazy the over jumps fox brown quick the"
        self.assertEqual(actual, expected)
