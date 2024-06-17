"""
unit tests
"""

from unittest import TestCase
from algorithms.topological_sort.find_all_possible_recipes_from_given_supplies.solution import Solution


class SolutionTestCase(TestCase):
    def test_cannot_make_recipes(self):
        # Given
        recipes = ["sandwich", "hamburger"]
        ingredients = [["bread", "bacon", "lettuce", "tomato"],
                       ["bun", "patty", "lettuce", "tomato"]]
        supplies = ["bacon", "lettuce", "tomato", "patty"]
        solution = Solution()

        # When
        actual = solution.find_recipes(recipes, ingredients, supplies)

        # Then
        expected = []
        self.assertEqual(actual, expected)

    def test_can_make_recipes(self):
        # Given
        recipes = ["sandwich", "hamburger"]
        ingredients = [["bread", "bacon", "lettuce", "tomato"],
                       ["bun", "patty", "lettuce", "tomato"]]
        supplies = ["bread", "bacon", "lettuce", "tomato", "bun", "patty"]
        solution = Solution()

        # When
        actual = solution.find_recipes(recipes, ingredients, supplies)

        # Then
        expected = ["sandwich", "hamburger"]
        self.assertEqual(actual, expected)

    def test_recipe_is_ingredient_of_other_recipe(self):
        # Given
        recipes = ["hamburger", "french fries", "hamburger and french fries"]
        ingredients = [["bun", "patty", "lettuce", "tomato"], [
            "potato", "ketchup"], ["hamburger", "french fries"]]
        supplies = ["lettuce", "tomato", "bun", "patty", "potato", "ketchup"]
        solution = Solution()

        # When
        actual = solution.find_recipes(recipes, ingredients, supplies)

        # Then
        expected = ["hamburger", "french fries", "hamburger and french fries"]
        self.assertEqual(actual, expected)
