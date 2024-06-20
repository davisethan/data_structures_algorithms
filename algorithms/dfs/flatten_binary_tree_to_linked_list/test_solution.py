"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.flatten_binary_tree_to_linked_list.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_flatten_tree(self):
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(7)
        root.left.left.left = BinaryTreeNode(8)
        root.left.left.right = BinaryTreeNode(9)
        root.left.right.left = BinaryTreeNode(10)
        root.left.right.right = BinaryTreeNode(11)
        root.right.left.left = BinaryTreeNode(12)
        root.right.left.right = BinaryTreeNode(13)
        root.right.right.left = BinaryTreeNode(14)
        root.right.right.right = BinaryTreeNode(15)
        solution = Solution()

        # When
        result = solution.flatten_tree(root)

        # Then
        current = result
        for n in [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]:
            self.assertEqual(current.data, n)
            self.assertEqual(current.left, None)
            current = current.right
