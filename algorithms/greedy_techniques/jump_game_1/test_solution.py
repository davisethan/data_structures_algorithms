"""
unit tests
"""

from unittest import TestCase
from algorithms.greedy_techniques.jump_game_1.solution import Solution


class SolutionTestCase(TestCase):
    def test_array_length_one(self):
        # Given
        numbers = [0]
        solution = Solution()

        # When
        actual = solution.jump_game(numbers)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_zero_at_start_failure(self):
        # Given
        numbers = [0, 4, 3, 2, 1, 0]
        solution = Solution()

        # When
        actual = solution.jump_game(numbers)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_zerio_at_middle_failure(self):
        # Given
        numbers = [4, 3, 2, 1, 0, 3, 2, 1, 0]
        solution = Solution()

        # When
        actual = solution.jump_game(numbers)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_success(self):
        # Given
        numbers = [4, 3, 2, 1, 0]
        solution = Solution()

        # When
        actual = solution.jump_game(numbers)

        # Then
        expected = True
        self.assertEqual(actual, expected)
