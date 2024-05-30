"""
unit tests
"""

from unittest import TestCase
from algorithms.k_way_merge.kth_smallest_number.solution import Solution


class SolutionTestCase(TestCase):
    def test_all_empty_lists(self):
        # Given
        lists = [[], [], [], [], []]
        k = 7
        solution = Solution()

        # When
        actual = solution.k_smallest_number(lists, k)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_some_empty_lists(self):
        # Given
        lists = [[], [1, 3, 5, 6, 9], [0, 2, 4, 6, 8], [], [-3, -2, -1, 0, 1]]
        k = 7
        solution = Solution()

        # When
        actual = solution.k_smallest_number(lists, k)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_empty_lists(self):
        # Given
        lists = [[53, 55, 57, 59], [35, 45, 55, 65], [
            49, 59, 69, 79], [20, 40, 60, 80], [101, 201, 301, 401]]
        k = 7
        solution = Solution()

        # When
        actual = solution.k_smallest_number(lists, k)

        # Then
        expected = 55
        self.assertEqual(actual, expected)

    def test_total_less_than_k(self):
        # Given
        lists = [[53, 55, 57, 59], [35, 45, 55, 65], [
            49, 59, 69, 79], [20, 40, 60, 80], [101, 201, 301, 401]]
        k = 30
        solution = Solution()

        # When
        actual = solution.k_smallest_number(lists, k)

        # Then
        expected = 401
        self.assertEqual(actual, expected)
