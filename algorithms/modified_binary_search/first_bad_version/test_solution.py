"""
unit tests
"""

from unittest import TestCase
from algorithms.modified_binary_search.first_bad_version.solution import Solution, API


class SolutionTestCase(TestCase):
    def test_first_bad_version_is_middle(self):
        # Given
        n = 20
        api = API(10)
        solution = Solution(api)

        # When
        actual = solution.first_bad_version(n)

        # Then
        expected = [10, 5]
        self.assertEqual(actual, expected)

    def test_first_bad_version_is_left_of_middle(self):
        # Given
        n = 20
        api = API(9)
        solution = Solution(api)

        # When
        actual = solution.first_bad_version(n)

        # Then
        expected = [9, 5]
        self.assertEqual(actual, expected)

    def test_first_bad_version_is_right_of_middle(self):
        # Given
        n = 20
        api = API(11)
        solution = Solution(api)

        # When
        actual = solution.first_bad_version(n)

        # Then
        expected = [11, 4]
        self.assertEqual(actual, expected)

    def test_first_bad_version_is_start(self):
        # Given
        n = 20
        api = API(1)
        solution = Solution(api)

        # When
        actual = solution.first_bad_version(n)

        # Then
        expected = [1, 4]
        self.assertEqual(actual, expected)

    def test_first_bad_version_is_end(self):
        # Given
        n = 20
        api = API(20)
        solution = Solution(api)

        # When
        actual = solution.first_bad_version(n)

        # Then
        expected = [20, 5]
        self.assertEqual(actual, expected)
