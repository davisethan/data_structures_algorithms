"""
unit tests
"""

from unittest import TestCase
from algorithms.k_way_merge.find_k_pairs_with_smallest_sums.solution import Solution


class SolutionTestCase(TestCase):
    def test_average_case(self):
        # Given
        list1 = [0, 4, 4, 5, 16, 17, 18]
        list2 = [3, 7, 8, 9, 16, 17, 19]
        k = 5
        solution = Solution()

        # When
        actual = solution.k_smallest_pairs(list1, list2, k)

        # Then
        expected = [(0, 3), (4, 3), (0, 7), (4, 3), (0, 8)]
        self.assertEqual(actual, expected)

    def test_index_out_of_range_prevented(self):
        # Given
        list1 = [0, 104, 104, 105, 116, 117, 118]
        list2 = [3, 7, 8, 9, 16, 17, 19]
        k = 8
        solution = Solution()

        # When
        actual = solution.k_smallest_pairs(list1, list2, k)

        # Then
        expected = [(0, 3), (0, 7), (0, 8), (0, 9),
                    (0, 16), (0, 17), (0, 19), (104, 3)]
        self.assertEqual(actual, expected)

    def test_number_of_pairs_less_than_k(self):
        # Given
        list1 = [0, 4, 4]
        list2 = [3, 7, 8]
        k = 100
        solution = Solution()

        # When
        actual = solution.k_smallest_pairs(list1, list2, k)

        # Then
        expected = [(0, 3), (4, 3), (4, 3), (0, 7), (0, 8),
                    (4, 7), (4, 7), (4, 8), (4, 8)]
        self.assertEqual(actual, expected)
