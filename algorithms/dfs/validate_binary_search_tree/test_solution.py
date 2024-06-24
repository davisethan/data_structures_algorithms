"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.validate_binary_search_tree.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_valid_bst(self):
        # Given
        root = BinaryTreeNode(9)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(11)
        root.left.left = BinaryTreeNode(-1)
        root.left.right = BinaryTreeNode(6)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(16)
        root.right.right.right = BinaryTreeNode(18)
        solution = Solution()

        # When
        actual = solution.validate_bst(root)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_invalid_bst(self):
        # Given
        root = BinaryTreeNode(9)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(11)
        root.left.left = BinaryTreeNode(-1)
        root.left.right = BinaryTreeNode(6)
        root.right.left = BinaryTreeNode(12)
        root.right.right = BinaryTreeNode(16)
        root.right.right.right = BinaryTreeNode(18)
        solution = Solution()

        # When
        actual = solution.validate_bst(root)

        # Then
        expected = False
        self.assertEqual(actual, expected)
