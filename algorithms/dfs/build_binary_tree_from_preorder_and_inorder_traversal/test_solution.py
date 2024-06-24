"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.build_binary_tree_from_preorder_and_inorder_traversal.solution import Solution


class SolutionTestCase(TestCase):
    def test_balanced_tree(self):
        # Given
        preorder = [-1, -7, -9, -18, -8, -4, -6, -3, 10, 6, 3, 9, 16, 11, 18]
        inorder = [-18, -9, -8, -7, -6, -4, -3, -1, 3, 6, 9, 10, 11, 16, 18]
        solution = Solution()

        # When
        root = solution.build_tree(preorder, inorder)
        actual = str(root)

        # Then
        expected = str(preorder)
        self.assertEqual(actual, expected)

    def test_left_skewed_tree(self):
        # Given
        preorder = [10, -4, -8, -9, -18, -6, -7, 3, -1, -3, 9, 6, 16, 11, 18]
        inorder = [-18, -9, -8, -7, -6, -4, -3, -1, 3, 6, 9, 10, 11, 16, 18]
        solution = Solution()

        # When
        root = solution.build_tree(preorder, inorder)
        actual = str(root)

        # Then
        expected = str(preorder)
        self.assertEqual(actual, expected)

    def test_degenerate_tree(self):
        # Given
        preorder = [-18, -9, -8, -7, -6, -4, -3, -1, 3, 6, 9, 10, 11, 16, 18]
        inorder = [-18, -9, -8, -7, -6, -4, -3, -1, 3, 6, 9, 10, 11, 16, 18]
        solution = Solution()

        # When
        root = solution.build_tree(preorder, inorder)
        actual = str(root)

        # Then
        expected = str(preorder)
        self.assertEqual(actual, expected)
