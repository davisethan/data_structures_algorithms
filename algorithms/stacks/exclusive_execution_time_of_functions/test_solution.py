"""
unit tests
"""

from unittest import TestCase
from algorithms.stacks.exclusive_execution_time_of_functions.solution import Solution


class SolutionTestCase(TestCase):
    def test_one_function_many_calls(self):
        # Given
        n = 1
        logs = ["0:start:0", "0:end:1", "0:start:2", "0:end:3", "0:start:4", "0:end:5",
                "0:start:6", "0:end:7", "0:start:8", "0:end:9", "0:start:10", "0:end:11"]
        solution = Solution()

        # When
        actual = solution.exclusive_time(n, logs)

        # Then
        expected = [12]
        self.assertEqual(actual, expected)

    def test_many_functions_one_call(self):
        # Given
        n = 6
        logs = ["0:start:0", "1:start:1", "2:start:2", "3:start:3", "4:start:4", "5:start:5",
                "5:end:6", "4:end:7", "3:end:8", "2:end:9", "1:end:10", "0:end:11"]
        solution = Solution()

        # When
        actual = solution.exclusive_time(n, logs)

        # Then
        expected = [2, 2, 2, 2, 2, 2]
        self.assertEqual(actual, expected)

    def test_many_functions_many_calls(self):
        # Given
        n = 6
        logs = ["0:start:0", "1:start:1", "2:start:2", "2:end:3", "1:end:4", "0:end:5",
                "3:start:6", "4:start:7", "5:start:8", "5:end:9", "4:end:10", "3:end:11"]
        solution = Solution()

        # When
        actual = solution.exclusive_time(n, logs)

        # Then
        expected = [2, 2, 2, 2, 2, 2]
        self.assertEqual(actual, expected)
