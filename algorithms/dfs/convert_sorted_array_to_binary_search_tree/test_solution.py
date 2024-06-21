"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.convert_sorted_array_to_binary_search_tree.solution import Solution


class SolutionTestCase(TestCase):
    def test_sorted_array_to_bst(self):
        # Given
        array = [-19, -18, -12, -10, -8, -6, -4, -3,
                 -2, 0, 1, 3, 4, 6, 7, 9, 11, 14, 15, 17]
        solution = Solution()

        # When
        result = solution.sorted_array_to_bst(array)

        # Then
        self.assertEqual(result.data, 0)
        self.assertEqual(result.left.data, -8)
        self.assertEqual(result.right.data, 7)
        self.assertEqual(result.left.left.data, -18)
        self.assertEqual(result.left.right.data, -4)
        self.assertEqual(result.right.left.data, 3)
        self.assertEqual(result.right.right.data, 14)
        self.assertEqual(result.left.left.left.data, -19)
        self.assertEqual(result.left.left.right.data, -12)
        self.assertEqual(result.left.right.left.data, -6)
        self.assertEqual(result.left.right.right.data, -3)
        self.assertEqual(result.right.left.left.data, 1)
        self.assertEqual(result.right.left.right.data, 4)
        self.assertEqual(result.right.right.left.data, 9)
        self.assertEqual(result.right.right.right.data, 15)
        self.assertEqual(result.left.left.right.right.data, -10)
        self.assertEqual(result.left.right.right.right.data, -2)
        self.assertEqual(result.right.left.right.right.data, 6)
        self.assertEqual(result.right.right.left.right.data, 11)
        self.assertEqual(result.right.right.right.right.data, 17)
