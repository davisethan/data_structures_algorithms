"""
unit tests
"""

from unittest import TestCase
from algorithms.modified_binary_search.search_rotated_sorted_array.solution import Solution


class SolutionTestCase(TestCase):
    def test_array_right_rotated_target_existent_left_of_middle_index(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 4
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 8
        self.assertEqual(actual, expected)

    def test_array_right_rotated_target_nonexistent_left_of_middle_index(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 2
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_array_right_rotated_target_existent_right_of_middle_index(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 6
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 10
        self.assertEqual(actual, expected)

    def test_array_right_rotated_target_non_existent_right_of_middle_index(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 7
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_array_right_rotated_target_is_existent_start_of_array(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 23
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_array_right_rotated_target_is_nonexistent_start_of_array(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 22
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_array_right_rotated_target_is_existent_end_of_array(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 21
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 19
        self.assertEqual(actual, expected)

    def test_array_right_rotated_target_is_nonexistent_end_of_array(self):
        # Given
        numbers = [23, 24, 25, 26, 28, 29, 0, 3, 4,
                   5, 6, 8, 9, 10, 12, 13, 16, 18, 19, 21]
        target = 30
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_existent_left_of_middle_index(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 24
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 8
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_nonexistent_left_of_middle_index(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 22
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_existent_right_of_middle_index(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 26
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 10
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_nonexistent_right_of_middle_index(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 27
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_is_existent_start_of_array(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 10
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_is_nonexistent_start_of_array(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 11
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_is_existent_end_of_array(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 9
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = 19
        self.assertEqual(actual, expected)

    def test_array_left_rotated_target_is_nonexistent_end_of_array(self):
        # Given
        numbers = [10, 12, 13, 16, 18, 19, 21, 23,
                   24, 25, 26, 28, 29, 0, 3, 4, 5, 6, 8, 9]
        target = 7
        solution = Solution()

        # When
        actual = solution.binary_search_rotated(numbers, target)

        # Then
        expected = -1
        self.assertEqual(actual, expected)
