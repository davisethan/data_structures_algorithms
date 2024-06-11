"""
unit tests
"""

from unittest import TestCase
from algorithms.backtracking.matchsticks_to_square.solution import Solution


class SolutionTestCase(TestCase):
    def test_solution_without_combinations(self):
        # Given
        matchsticks = [1, 1, 1, 1]
        solution = Solution()

        # When
        actual = solution.matchsticks_to_square(matchsticks)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_solution_with_combinations(self):
        # Given
        matchsticks = [1, 2, 3, 4, 6, 7, 8, 9]
        solution = Solution()

        # When
        actual = solution.matchsticks_to_square(matchsticks)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_no_solution(self):
        # Given
        matchsticks = [1, 2, 3, 4, 5]
        solution = Solution()

        # When
        actual = solution.matchsticks_to_square(matchsticks)

        # Then
        expected = False
        self.assertEqual(actual, expected)
