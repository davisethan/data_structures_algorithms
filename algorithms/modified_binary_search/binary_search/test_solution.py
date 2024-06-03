"""
unit tests
"""

from unittest import TestCase
from algorithms.modified_binary_search.binary_search.solution import Solution


class SolutionTestCase(TestCase):
    def test_target_is_first_middle(self):
        # Given
        numbers = [1, 3, 4, 8, 9, 10, 11, 12, 13, 15,
                   16, 17, 18, 20, 21, 22, 23, 25, 26, 29]
        target = 16
        solution = Solution()

        # When
        actual = solution.binary_search(numbers, target)

        # Then
        expected = 10
        self.assertEqual(actual, expected)

    def test_target_is_left_of_first_middle(self):
        # Given
        numbers = [1, 3, 4, 8, 9, 10, 11, 12, 13, 15,
                   16, 17, 18, 20, 21, 22, 23, 25, 26, 29]
        target = 15
        solution = Solution()

        # When
        actual = solution.binary_search(numbers, target)

        # Then
        expected = 9
        self.assertEqual(actual, expected)

    def test_target_is_right_of_first_middle(self):
        # Given
        numbers = [1, 3, 4, 8, 9, 10, 11, 12, 13, 15,
                   16, 17, 18, 20, 21, 22, 23, 25, 26, 29]
        target = 17
        solution = Solution()

        # When
        actual = solution.binary_search(numbers, target)

        # Then
        expected = 11
        self.assertEqual(actual, expected)

    def test_target_is_start(self):
        # Given
        numbers = [1, 3, 4, 8, 9, 10, 11, 12, 13, 15,
                   16, 17, 18, 20, 21, 22, 23, 25, 26, 29]
        target = 1
        solution = Solution()

        # When
        actual = solution.binary_search(numbers, target)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_target_is_end(self):
        # Given
        numbers = [1, 3, 4, 8, 9, 10, 11, 12, 13, 15,
                   16, 17, 18, 20, 21, 22, 23, 25, 26, 29]
        target = 29
        solution = Solution()

        # When
        actual = solution.binary_search(numbers, target)

        # Then
        expected = 19
        self.assertEqual(actual, expected)

    def test_target_nonexistent(self):
        # Given
        numbers = [1, 3, 4, 8, 9, 10, 11, 12, 13, 15,
                   16, 17, 18, 20, 21, 22, 23, 25, 26, 29]
        target = 55
        solution = Solution()

        # When
        actual = solution.binary_search(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)
