"""
unit tests
"""

from unittest import TestCase
from algorithms.cyclic_sort.find_corrupt_pair.solution import Solution


class SolutionTestCase(TestCase):
    def test_first_integer_is_corrupted(self):
        # Given
        numbers = [13, 2, 9, 6, 11, 19, 5, 17, 20,
                   15, 10, 8, 7, 4, 18, 1, 14, 3, 12, 16, 1]
        solution = Solution()

        # When
        actual = solution.find_corrupt_pair(numbers)

        # Then
        expected = [21, 1]
        self.assertEqual(actual, expected)

    def test_last_integer_is_corrupted(self):
        # Given
        numbers = [13, 2, 9, 6, 11, 19, 5, 17, 20,
                   15, 10, 8, 7, 4, 18, 1, 14, 3, 12, 16, 11]
        solution = Solution()

        # When
        actual = solution.find_corrupt_pair(numbers)

        # Then
        expected = [21, 11]
        self.assertEqual(actual, expected)

    def test_middle_integer_is_corrupted(self):
        # Given
        numbers = [13, 2, 9, 6, 11, 19, 5, 17, 20,
                   15, 10, 8, 7, 4, 18, 1, 14, 3, 12, 16, 20]
        solution = Solution()

        # When
        actual = solution.find_corrupt_pair(numbers)

        # Then
        expected = [21, 20]
        self.assertEqual(actual, expected)
