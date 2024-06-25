"""
unit tests
"""

from unittest import TestCase
from algorithms.bfs.symmetric_tree.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_left_skewed_tree(self):
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(5)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(5)
        root.right.right = BinaryTreeNode(5)
        root.left.left.left = BinaryTreeNode(7)
        root.left.left.right = BinaryTreeNode(7)
        root.left.right.left = BinaryTreeNode(7)
        root.left.right.right = BinaryTreeNode(7)
        solution = Solution()

        # When
        actual = solution.is_symmetric(root)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_data_mismatch(self):
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(5)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(7)
        root.right.right = BinaryTreeNode(7)
        solution = Solution()

        # When
        actual = solution.is_symmetric(root)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_binary_tree_succeeds(self):
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(5)
        root.right.right = BinaryTreeNode(5)
        root.left.left.left = BinaryTreeNode(7)
        root.right.right.right = BinaryTreeNode(7)
        solution = Solution()

        # When
        actual = solution.is_symmetric(root)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_perfect_binary_tree_succeeds(self):
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(5)
        root.left.right = BinaryTreeNode(7)
        root.right.left = BinaryTreeNode(7)
        root.right.right = BinaryTreeNode(5)
        solution = Solution()

        # When
        actual = solution.is_symmetric(root)

        # Then
        expected = True
        self.assertEqual(actual, expected)
