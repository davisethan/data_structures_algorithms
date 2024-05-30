"""
unit tests
"""

from unittest import TestCase
from algorithms.k_way_merge.merge_sorted_array.solution import Solution


class SolutionTestCase(TestCase):
    def test_first_array_greater_length(self):
        # Given
        nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 0, 0, 0, 0]
        nums2 = [2, 4, 6, 8, 10]
        m, n = 10, 5
        solution = Solution()

        # When
        actual = solution.merge_sorted(nums1, m, nums2, n)

        # Then
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19]
        self.assertEqual(actual, expected)

    def test_second_array_greater_length(self):
        # Given
        nums1 = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        m, n = 5, 10
        solution = Solution()

        # When
        actual = solution.merge_sorted(nums1, m, nums2, n)

        # Then
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]
        self.assertEqual(actual, expected)
