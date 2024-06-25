"""
unit tests
"""

from unittest import TestCase
from algorithms.bfs.vertical_order_traversal_of_binary_tree.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_vertical_order(self):
        # Given
        root = BinaryTreeNode(-6)
        root.left = BinaryTreeNode(-15)
        root.right = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(-18)
        root.left.right = BinaryTreeNode(-11)
        root.right.left = BinaryTreeNode(1)
        root.right.right = BinaryTreeNode(17)
        root.left.left.left = BinaryTreeNode(-19)
        root.left.left.right = BinaryTreeNode(-17)
        root.left.right.left = BinaryTreeNode(-12)
        root.left.right.right = BinaryTreeNode(-8)
        root.right.left.left = BinaryTreeNode(-5)
        root.right.left.right = BinaryTreeNode(6)
        root.right.right.left = BinaryTreeNode(13)
        root.right.right.right = BinaryTreeNode(20)
        solution = Solution()

        # When
        actual = solution.vertical_order(root)

        # Then
        expected = [[-19], [-18], [-15, -17, -12, -5],
                    [-6, -11, 1], [7, -8, 6, 13], [17], [20]]
        self.assertEqual(actual, expected)
