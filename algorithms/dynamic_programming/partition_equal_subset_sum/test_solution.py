"""
unit tests
"""

from unittest import TestCase
from algorithms.dynamic_programming.partition_equal_subset_sum.solution import Solution


class SolutionTestCase(TestCase):
    def test_odd_sum_nonexistent_solution(self):
        # Given
        numbers = [20, 17, 24, 15, 21, 22, 17, 19]
        solution = Solution()

        # When
        actual = solution.can_partition_array(numbers)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_even_sum_nonexistent_solution(self):
        # Given
        numbers = [2, 2, 2, 4, 6, 6, 8, 8]
        solution = Solution()

        # When
        actual = solution.can_partition_array(numbers)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_even_sum_existent_solution(self):
        # Given
        numbers = [20, 17, 24, 15, 21, 22, 16, 19]
        solution = Solution()

        # When
        actual = solution.can_partition_array(numbers)

        # Then
        expected = True
        self.assertEqual(actual, expected)
