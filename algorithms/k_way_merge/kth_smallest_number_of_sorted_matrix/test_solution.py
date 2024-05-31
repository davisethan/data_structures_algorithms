"""
unit tests
"""

from unittest import TestCase
from algorithms.k_way_merge.kth_smallest_number_of_sorted_matrix.solution import Solution


class SolutionTestCase(TestCase):
    def test_empty_matrix(self):
        # Given
        matrix = []
        k = 7
        solution = Solution()

        # When
        actual = solution.kth_smallest_number(matrix, k)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_matrix_smaller_than_k(self):
        # Given
        matrix = [[24, 26],
                  [34, 36]]
        k = 7
        solution = Solution()

        # When
        actual = solution.kth_smallest_number(matrix, k)

        # Then
        expected = 36
        self.assertEqual(actual, expected)

    def test_matrix_larger_than_k(self):
        # Given
        matrix = [[51, 53, 55, 57, 59],
                  [61, 63, 65, 67, 69],
                  [71, 73, 75, 77, 79],
                  [81, 83, 85, 87, 89],
                  [91, 93, 95, 97, 99]]
        k = 7
        solution = Solution()

        # When
        actual = solution.kth_smallest_number(matrix, k)

        # Then
        expected = 63
        self.assertEqual(actual, expected)
