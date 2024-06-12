"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.counting_bits.solution import Solution


class SolutionTestCase(TestCase):
    def test_n_is_base_case(self):
        # Given
        n = 0
        solution = Solution()

        # When
        actual = solution.counting_bits(n)

        # Then
        expected = [0]
        self.assertEqual(actual, expected)

    def test_n_is_not_base_case(self):
        # Given
        n = 15
        solution = Solution()

        # When
        actual = solution.counting_bits(n)

        # Then
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        self.assertEqual(actual, expected)
