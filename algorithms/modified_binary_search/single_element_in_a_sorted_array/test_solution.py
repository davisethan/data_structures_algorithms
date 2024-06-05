"""
unit tests
"""

from unittest import TestCase
from algorithms.modified_binary_search.single_element_in_a_sorted_array.solution import Solution


class SolutionTestCase(TestCase):
    def test_odd_parity_middle_with_single_at_middle(self):
        # Given
        numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        solution = Solution()

        # Then
        actual = solution.single_non_duplicate(numbers)

        # When
        expected = 4
        self.assertEqual(actual, expected)

    def test_odd_parity_middle_with_single_at_start(self):
        # Given
        numbers = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        solution = Solution()

        # When
        actual = solution.single_non_duplicate(numbers)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_odd_parity_middle_with_single_at_end(self):
        # Given
        numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]
        solution = Solution()

        # When
        actual = solution.single_non_duplicate(numbers)

        # Then
        expected = 9
        self.assertEqual(actual, expected)

    def test_even_parity_middle_with_single_at_middle(self):
        # Given
        numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4,
                   5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        solution = Solution()

        # When
        actual = solution.single_non_duplicate(numbers)

        # Then
        expected = 5
        self.assertEqual(actual, expected)

    def test_even_parity_middle_with_single_at_start(self):
        # Given
        numbers = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5,
                   5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        solution = Solution()

        # When
        actual = solution.single_non_duplicate(numbers)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_even_parity_middle_with_single_at_end(self):
        # Given
        numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4,
                   4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
        solution = Solution()

        # When
        actual = solution.single_non_duplicate(numbers)

        # Then
        expected = 10
        self.assertEqual(actual, expected)
