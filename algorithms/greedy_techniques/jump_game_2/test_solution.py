"""
unit tests
"""

from unittest import TestCase
from algorithms.greedy_techniques.jump_game_2.solution import Solution


class SolutionTestCase(TestCase):
    def test_no_steps_to_last_index(self):
        # Given
        numbers = [0]
        solution = Solution()

        # When
        actual = solution.jump_game(numbers)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_some_steps_to_last_index(self):
        # Given
        numbers = [3, 1, 4, 2, 5, 3, 1, 4, 2, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        solution = Solution()

        # When
        actual = solution.jump_game(numbers)

        # Then
        expected = 5
        self.assertEqual(actual, expected)
