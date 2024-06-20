"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.diameter_of_binary_tree.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_diameter_passes_through_root(self):
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(7)
        root.left.left.left = BinaryTreeNode(8)
        root.left.right.left = BinaryTreeNode(9)
        root.right.left.left = BinaryTreeNode(10)
        root.right.right.left = BinaryTreeNode(11)
        solution = Solution()

        # When
        actual = solution.diameter_of_binary_tree(root)

        # Then
        expected = 6
        self.assertEqual(actual, expected)

    def test_diameter_doesnt_pass_throuh_root(self):
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.right.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(5)
        root.right.right.left = BinaryTreeNode(6)
        root.right.right.right = BinaryTreeNode(7)
        root.right.right.left.left = BinaryTreeNode(8)
        root.right.right.right.left = BinaryTreeNode(9)
        root.right.right.left.left.left = BinaryTreeNode(10)
        root.right.right.right.left.left = BinaryTreeNode(11)
        root.right.right.left.left.left.left = BinaryTreeNode(12)
        root.right.right.right.left.left.left = BinaryTreeNode(13)
        solution = Solution()

        # When
        actual = solution.diameter_of_binary_tree(root)

        # Then
        expected = 8
        self.assertEqual(actual, expected)
