"""
unit tests
"""

from unittest import TestCase
from algorithms.hashmaps.next_greater_element.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_next_greater_elements(self):
        # Given
        n2 = [15, 13, 11, 9, 7, 5, 3, 1]
        n1 = [15, 11, 7, 3]
        solution = Solution()

        # When
        actual = solution.next_greater_element(n1, n2)

        # Then
        expected = [-1, -1, -1, -1]
        self.assertEqual(actual, expected)

    def test_some_next_greater_elements(self):
        # Given
        n2 = [0, 4, -6, -13, 15, -8, -15, 5, 20, -10, 12, 10]
        n1 = [4, -13, -8, 5, -10, 10]
        solution = Solution()

        # When
        actual = solution.next_greater_element(n1, n2)

        # Then
        expected = [15, 15, 5, 20, 12, -1]
        self.assertEqual(actual, expected)

    def test_all_next_greater_elements(self):
        # Given
        n2 = [1, 3, 5, 7, 9, 11, 13, 15]
        n1 = [1, 5, 9, 13]
        solution = Solution()

        # When
        actual = solution.next_greater_element(n1, n2)

        # Then
        expected = [3, 7, 11, 15]
        self.assertEqual(actual, expected)
