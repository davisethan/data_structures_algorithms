"""
unit tests
"""

from unittest import TestCase
from algorithms.sliding_window.best_time_to_buy_and_sell_stock.solution import Solution


class SolutionTestCase(TestCase):
    def test_empty_prices(self):
        # Given
        prices = list()
        solution = Solution()

        # When
        actual = solution.max_profit(prices)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_striclty_decreasing_prices(self):
        # Given
        prices = [10, 8, 6, 4, 2]
        solution = Solution()

        # When
        actual = solution.max_profit(prices)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_strictly_increasing_prices(self):
        # Given
        prices = [2, 4, 6, 8, 10]
        solution = Solution()

        # When
        actual = solution.max_profit(prices)

        # Then
        expected = 8
        self.assertEqual(actual, expected)

    def test_two_peaks_return_first(self):
        # Given
        prices = [6, 8, 10, 12, 4, 6, 8]
        solution = Solution()

        # When
        actual = solution.max_profit(prices)

        # Then
        expected = 6
        self.assertEqual(actual, expected)

    def test_two_peaks_return_second(self):
        # Given
        prices = [4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11]
        solution = Solution()

        # When
        actual = solution.max_profit(prices)

        # Then
        expected = 10
        self.assertEqual(actual, expected)
