"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.binary_tree_right_side_view.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_balanced_tree(self):
        # Given
        root = BinaryTreeNode(-1)
        root.left = BinaryTreeNode(-7)
        root.right = BinaryTreeNode(10)
        root.left.left = BinaryTreeNode(-9)
        root.left.right = BinaryTreeNode(-4)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(16)
        root.left.left.left = BinaryTreeNode(-18)
        root.left.left.right = BinaryTreeNode(-8)
        root.left.right.left = BinaryTreeNode(-6)
        root.left.right.right = BinaryTreeNode(-3)
        root.right.left.left = BinaryTreeNode(3)
        root.right.left.right = BinaryTreeNode(9)
        root.right.right.left = BinaryTreeNode(11)
        root.right.right.right = BinaryTreeNode(18)
        solution = Solution()

        # When
        actual = solution.right_side_view(root)

        # Then
        expected = [-1, 10, 16, 18]
        self.assertEqual(actual, expected)

    def test_left_skewed_tree(self):
        # Given
        root = BinaryTreeNode(10)
        root.left = BinaryTreeNode(-4)
        root.right = BinaryTreeNode(16)
        root.left.left = BinaryTreeNode(-8)
        root.left.right = BinaryTreeNode(3)
        root.right.left = BinaryTreeNode(11)
        root.right.right = BinaryTreeNode(18)
        root.left.left.left = BinaryTreeNode(-9)
        root.left.left.right = BinaryTreeNode(-6)
        root.left.right.left = BinaryTreeNode(-1)
        root.left.right.right = BinaryTreeNode(9)
        root.left.left.left.left = BinaryTreeNode(-18)
        root.left.left.right.left = BinaryTreeNode(-7)
        root.left.right.left.left = BinaryTreeNode(-3)
        root.left.right.right.left = BinaryTreeNode(6)
        solution = Solution()

        # When
        actual = solution.right_side_view(root)

        # Then
        expected = [10, 16, 18, 9, 6]
        self.assertEqual(actual, expected)

    def test_degenerate_tree(self):
        # Given
        root = BinaryTreeNode(-1)
        root.left = BinaryTreeNode(3)
        root.left.right = BinaryTreeNode(6)
        root.left.right.left = BinaryTreeNode(9)
        root.left.right.left.right = BinaryTreeNode(10)
        root.left.right.left.right.left = BinaryTreeNode(11)
        root.left.right.left.right.left.right = BinaryTreeNode(16)
        root.left.right.left.right.left.right.left = BinaryTreeNode(18)
        solution = Solution()

        # When
        actual = solution.right_side_view(root)

        # Then
        expected = [-1, 3, 6, 9, 10, 11, 16, 18]
        self.assertEqual(actual, expected)
