"""
unit tests
"""

from unittest import TestCase
from algorithms.top_k_elements.kth_largest_element_of_stream.solution import KthLargest


class SolutionTestCase(TestCase):
    def test_small_stream(self):
        # Given
        k = 7
        nums = [7, 13, 29, 11, 23, 2, 19, 5, 21, 26, 17, 0, 14, 8, 25]
        kth_largest = KthLargest(k, nums)

        # When
        actual = kth_largest.heap.top()

        # Then
        expected = 17
        self.assertEqual(actual, expected)

    def test_large_stream(self):
        # Given
        k = 7
        nums = [34, 67, 250, 99, 301, 483, 76, 192, 456, 127, 348, 284, 13, 222, 401, 178, 69, 415, 230, 351, 82, 245, 300, 157, 60, 197, 412, 268, 91, 145, 377, 110, 44, 256, 309, 118, 35, 269, 325, 214, 275, 158, 71, 485, 48, 124, 205, 226, 286, 19,
                342, 289, 223, 67, 434, 57, 143, 188, 241, 177, 122, 316, 159, 379, 248, 173, 31, 149, 96, 317, 95, 333, 290, 134, 245, 215, 400, 49, 392, 367, 14, 107, 284, 371, 173, 93, 483, 52, 199, 28, 259, 233, 64, 315, 445, 224, 161, 312, 389, 417]
        kth_largest = KthLargest(k, nums)

        # When
        actual = kth_largest.heap.top()

        # Then
        expected = 417
        self.assertEqual(actual, expected)
