"""
unit tests
"""

from unittest import TestCase
from algorithms.modified_binary_search.search_rotated_sorted_array_2.solution import Solution


class SolutionTestCase(TestCase):
    def test_constant_numbers_and_nonexistent_target(self):
        # Given
        numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 3
        solution = Solution()

        # When
        actual = solution.search(numbers, target)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_constant_numbers_and_existent_target_at_left_of_middle(self):
        # Given
        numbers = [1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 3
        solution = Solution()

        # When
        actual = solution.search(numbers, target)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_constant_numbers_and_existent_target_at_right_of_middle(self):
        # Given
        numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 3
        solution = Solution()

        # When
        actual = solution.search(numbers, target)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_constant_numbers_and_existent_target_at_start(self):
        # Given
        numbers = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 3
        solution = Solution()

        # When
        actual = solution.search(numbers, target)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_constant_numbers_and_existent_target_at_end(self):
        # Given
        numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
        target = 3
        solution = Solution()

        # When
        actual = solution.search(numbers, target)

        # Then
        expected = True
        self.assertEqual(actual, expected)
