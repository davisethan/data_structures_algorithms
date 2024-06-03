"""
unit tests
"""

from unittest import TestCase
from algorithms.top_k_elements.kth_largest_element_of_array.solution import Solution


class SolutionTestCase(TestCase):
    def test_no_duplicates(self):
        # Given
        numbers = [51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]
        k = 7
        solution = Solution()

        # When
        actual = solution.find_kth_largest(numbers, k)

        # Then
        expected = 77
        self.assertEqual(actual, expected)

    def test_some_duplicates(self):
        # Given
        numbers = [51, 53, 55, 57, 59, 71, 71, 73, 73, 75, 75, 77, 77, 79, 79]
        k = 9
        solution = Solution()

        # When
        actual = solution.find_kth_largest(numbers, k)

        # Then
        expected = 71
        self.assertEqual(actual, expected)
