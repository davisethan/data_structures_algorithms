"""
unit tests
"""

from unittest import TestCase
from algorithms.modified_binary_search.find_k_closest_elements.solution import Solution


class SolutionTestCase(TestCase):
    def test_array_length_k(self):
        # Given
        numbers = [1, 3, 5, 6, 7, 8, 9, 10, 12, 16,
                   19, 21, 24, 25, 27, 30, 32, 34, 37, 39]
        target = 16
        k = 20
        solution = Solution()

        # When
        actual = solution.find_closest_elements(numbers, target, k)

        # Then
        expected = [1, 3, 5, 6, 7, 8, 9, 10, 12, 16,
                    19, 21, 24, 25, 27, 30, 32, 34, 37, 39]
        self.assertEqual(actual, expected)

    def test_target_below_start(self):
        # Given
        numbers = [1, 3, 5, 6, 7, 8, 9, 10, 12, 16,
                   19, 21, 24, 25, 27, 30, 32, 34, 37, 39]
        target = -10
        k = 5
        solution = Solution()

        # When
        actual = solution.find_closest_elements(numbers, target, k)

        # Then
        expected = [1, 3, 5, 6, 7]
        self.assertEqual(actual, expected)

    def test_target_above_start(self):
        # Given
        numbers = [1, 3, 5, 6, 7, 8, 9, 10, 12, 16,
                   19, 21, 24, 25, 27, 30, 32, 34, 37, 39]
        target = 40
        k = 5
        solution = Solution()

        # When
        actual = solution.find_closest_elements(numbers, target, k)

        # Then
        expected = [30, 32, 34, 37, 39]
        self.assertEqual(actual, expected)

    def test_target_at_start(self):
        # Given
        numbers = [1, 3, 5, 6, 7, 8, 9, 10, 12, 16,
                   19, 21, 24, 25, 27, 30, 32, 34, 37, 39]
        target = 1
        k = 5
        solution = Solution()

        # When
        actual = solution.find_closest_elements(numbers, target, k)

        # Then
        expected = [1, 3, 5, 6, 7]
        self.assertEqual(actual, expected)

    def test_target_at_end(self):
        # Given
        numbers = [1, 3, 5, 6, 7, 8, 9, 10, 12, 16,
                   19, 21, 24, 25, 27, 30, 32, 34, 37, 39]
        target = 39
        k = 5
        solution = Solution()

        # When
        actual = solution.find_closest_elements(numbers, target, k)

        # Then
        expected = [30, 32, 34, 37, 39]
        self.assertEqual(actual, expected)

    def test_nearest_above_and_below(self):
        # Given
        numbers = [-9, -7, -5, -3, -1, 0, 1, 3, 5, 7, 9]
        target = 0
        k = 6
        solution = Solution()

        # When
        actual = solution.find_closest_elements(numbers, target, k)

        # Then
        expected = [-5, -3, -1, 0, 1, 3]
        self.assertEqual(actual, expected)
