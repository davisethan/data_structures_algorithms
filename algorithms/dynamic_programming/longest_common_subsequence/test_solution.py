"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.longest_common_subsequence.solution import Solution


class SolutionTestCase(TestCase):
    def test_nonexistent_common_subsequence(self):
        # Given
        s1 = "abcdefgh"
        s2 = "stuvwxyz"
        solution = Solution()

        # When
        actual = solution.longest_common_subsequence(s1, s2)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_existent_common_subsequence_earlier_in_first_string(self):
        # Given
        s1 = "ijkabcdpqrst"
        s2 = "tsrqpabcdkji"
        solution = Solution()

        # When
        actual = solution.longest_common_subsequence(s1, s2)

        # Then
        expected = 4
        self.assertEqual(actual, expected)

    def test_existent_common_subsequence_earlier_in_second_string(self):
        # Given
        s1 = "tsrqpabcdkji"
        s2 = "ijkabcdpqrst"
        solution = Solution()

        # When
        actual = solution.longest_common_subsequence(s1, s2)

        # Then
        expected = 4
        self.assertEqual(actual, expected)
