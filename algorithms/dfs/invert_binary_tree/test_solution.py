"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.invert_binary_tree.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_invert_binary_tree(self):
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
        result = solution.mirror_binary_tree(root)

        # Then
        self.assertEqual(result.data, 1)
        self.assertEqual(result.left.data, 3)
        self.assertEqual(result.right.data, 2)
        self.assertEqual(result.left.left.data, 7)
        self.assertEqual(result.left.right.data, 6)
        self.assertEqual(result.right.left.data, 5)
        self.assertEqual(result.right.right.data, 4)
        self.assertEqual(result.left.left.right.data, 11)
        self.assertEqual(result.left.right.right.data, 10)
        self.assertEqual(result.right.left.right.data, 9)
        self.assertEqual(result.right.right.right.data, 8)
