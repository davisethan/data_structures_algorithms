"""
unit tests
"""

from unittest import TestCase
from algorithms.hashmaps.isomorphic_strings.solution import Solution


class SolutionTestCase(TestCase):
    def test_is_isomorphic_fails(self):
        # Given
        s1 = "xmtdkjswqblefinxgcvp"
        s2 = "xmtdkjswqblefQQQgcvp"
        solution = Solution()

        # When
        actual = solution.is_isomorphic(s1, s2)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_is_isomorphic_succeeds(self):
        # Given
        s1 = "xmtdkjswqblefinxgcvp"
        s2 = "xmtdkjswqblefinxgcvp"
        solution = Solution()

        # When
        actual = solution.is_isomorphic(s1, s2)

        # Then
        expected = True
        self.assertEqual(actual, expected)
