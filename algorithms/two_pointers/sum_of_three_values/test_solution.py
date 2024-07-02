"""
unit tests
"""

from unittest import TestCase
from algorithms.two_pointers.sum_of_three_values.solution import Solution


class SolutionTestCase(TestCase):
    def test_sum_of_three_values_fails(self):
        # Given
        numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 52
        solution = Solution()

        # When
        actual = solution.find_sum_of_three(numbers, target)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_sum_of_three_values_succeeds(self):
        # Given
        numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 51
        solution = Solution()

        # When
        actual = solution.find_sum_of_three(numbers, target)

        # Then
        expected = True
        self.assertEqual(actual, expected)
