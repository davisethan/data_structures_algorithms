"""
unit tests
"""

from unittest import TestCase
from algorithms.two_heaps.sliding_window_median.solution import Solution


class SolutionTestCase(TestCase):
    def test_strictly_increasing_array_even_length_subarray(self):
        # Given
        nums = [1, 2, 5, 6, 8, 10, 12, 16, 17, 18, 20, 21, 23, 26, 30,
                31, 34, 37, 38, 40, 41, 45, 48, 49, 51, 53, 55, 56, 57, 59]
        k = 4
        solution = Solution()

        # When
        actual = solution.median_sliding_window(nums, k)

        # Then
        expected = [3.5, 5.5, 7.0, 9.0, 11.0, 14.0, 16.5, 17.5, 19.0, 20.5, 22.0, 24.5, 28.0,
                    30.5, 32.5, 35.5, 37.5, 39.0, 40.5, 43.0, 46.5, 48.5, 50.0, 52.0, 54.0, 55.5, 56.5]
        self.assertEqual(actual, expected)

    def test_strictly_increasing_array_odd_length_subarray(self):
        # Given
        nums = [1, 2, 5, 6, 8, 10, 12, 16, 17, 18, 20, 21, 23, 26, 30,
                31, 34, 37, 38, 40, 41, 45, 48, 49, 51, 53, 55, 56, 57, 59]
        k = 5
        solution = Solution()

        # When
        actual = solution.median_sliding_window(nums, k)

        # Then
        expected = [5, 6, 8, 10, 12, 16, 17, 18, 20, 21, 23, 26,
                    30, 31, 34, 37, 38, 40, 41, 45, 48, 49, 51, 53, 55, 56]
        self.assertEqual(actual, expected)

    def test_strictly_decreasing_array_even_length_subarray(self):
        # Given
        nums = [58, 53, 51, 50, 49, 47, 46, 44, 42, 39, 37, 35, 33, 31,
                30, 29, 28, 24, 23, 20, 18, 17, 16, 15, 13, 9, 8, 5, 4, 1]
        k = 4
        solution = Solution()

        # When
        actual = solution.median_sliding_window(nums, k)

        # Then
        expected = [52.0, 50.5, 49.5, 48.0, 46.5, 45.0, 43.0, 40.5, 38.0, 36.0, 34.0, 32.0,
                    30.5, 29.5, 28.5, 26.0, 23.5, 21.5, 19.0, 17.5, 16.5, 15.5, 14.0, 11.0, 8.5, 6.5, 4.5]
        self.assertEqual(actual, expected)

    def test_strictly_decreasing_array_odd_length_subarray(self):
        # Given
        nums = [58, 53, 51, 50, 49, 47, 46, 44, 42, 39, 37, 35, 33, 31,
                30, 29, 28, 24, 23, 20, 18, 17, 16, 15, 13, 9, 8, 5, 4, 1]
        k = 5
        solution = Solution()

        # When
        actual = solution.median_sliding_window(nums, k)

        # Then
        expected = [51, 50, 49, 47, 46, 44, 42, 39, 37, 35, 33, 31,
                    30, 29, 28, 24, 23, 20, 18, 17, 16, 15, 13, 9, 8, 5]
        self.assertEqual(actual, expected)

    def test_random_array_even_length_subarray(self):
        # Given
        nums = [38, 20, 9, 31, 55, 44, 42, 18, 34, 5, 16, 37, 52, 47,
                26, 6, 2, 36, 11, 43, 59, 15, 10, 51, 56, 48, 7, 33, 27, 28]
        k = 4
        solution = Solution()

        # When
        actual = solution.median_sliding_window(nums, k)

        # Then
        expected = [25.5, 25.5, 37.5, 43.0, 43.0, 38.0, 26.0, 17.0, 25.0, 26.5, 42.0, 42.0, 36.5,
                    16.0, 16.0, 8.5, 23.5, 39.5, 29.0, 29.0, 33.0, 33.0, 49.5, 49.5, 40.5, 30.0, 27.5]
        self.assertEqual(actual, expected)

    def test_random_array_odd_length_subarray(self):
        # Given
        nums = [38, 20, 9, 31, 55, 44, 42, 18, 34, 5, 16, 37, 52, 47,
                26, 6, 2, 36, 11, 43, 59, 15, 10, 51, 56, 48, 7, 33, 27, 28]
        k = 5
        solution = Solution()

        # When
        actual = solution.median_sliding_window(nums, k)

        # Then
        expected = [31, 31, 42, 42, 42, 34, 18, 18, 34, 37, 37, 37,
                    26, 26, 11, 11, 36, 36, 15, 43, 51, 48, 48, 48, 33, 28]
        self.assertEqual(actual, expected)
