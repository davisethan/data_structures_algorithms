"""
unit tests
"""

from unittest import TestCase
from algorithms.greedy_techniques.boats_to_save_people.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_life_boat_pairs(self):
        # Given
        people = [234, 246, 236, 229, 247, 258, 249, 235, 244, 239]
        limit = 200
        solution = Solution()

        # When
        actual = solution.rescue_boats(people, limit)

        # Then
        expected = 10
        self.assertEqual(actual, expected)

    def test_all_life_boat_pairs(self):
        # Given
        people = [150, 185, 120, 103, 130, 169, 158, 144, 131, 143]
        limit = 400
        solution = Solution()

        # When
        actual = solution.rescue_boats(people, limit)

        # Then
        expected = 5
        self.assertEqual(actual, expected)

    def test_some_life_boat_pairs(self):
        # Given
        people = [335, 143, 312, 140, 355, 110, 347, 142, 341, 107, 354, 103]
        limit = 300
        solution = Solution()

        # When
        actual = solution.rescue_boats(people, limit)

        # Then
        expected = 9
        self.assertEqual(actual, expected)

    def test_odd_number_of_people(self):
        # Given
        people = [335, 143, 312, 140, 355, 110,
                  347, 142, 341, 107, 354, 103, 111]
        limit = 300
        solution = Solution()

        # When
        actual = solution.rescue_boats(people, limit)

        # Then
        expected = 10
        self.assertEqual(actual, expected)
