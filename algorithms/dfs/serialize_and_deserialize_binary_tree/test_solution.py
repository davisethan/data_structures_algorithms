"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.serialize_and_deserialize_binary_tree.solution import Solution


class SolutionTestCase(TestCase):
    def test_deserialize_and_serialize(self):
        # Given
        stream = [1, 2, 4, 8, None, 5, 9, None, 3, 6, 10, None, 7,
                  11, None, None, None, None, None, None, None, None, None]
        solution = Solution()

        # When
        actual = solution.serialize(solution.deserialize(stream))

        # Then
        expected = stream
        self.assertEqual(actual, expected)
