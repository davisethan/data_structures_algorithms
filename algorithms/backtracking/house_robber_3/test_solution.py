"""
unit tests
"""

from unittest import TestCase
from algorithms.backtracking.house_robber_3.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_root_included(self):
        # Given
        root = BinaryTreeNode(55)
        root.left = BinaryTreeNode(15)
        root.right = BinaryTreeNode(23)
        root.left.left = BinaryTreeNode(5)
        root.left.right = BinaryTreeNode(3)
        root.right.left = BinaryTreeNode(8)
        root.right.right = BinaryTreeNode(9)
        solution = Solution()

        # When
        actual = solution.rob(root)

        # Then
        expected = 80
        self.assertEqual(actual, expected)

    def test_left_child_and_right_child_included(self):
        # Given
        root = BinaryTreeNode(55)
        root.left = BinaryTreeNode(45)
        root.right = BinaryTreeNode(38)
        root.left.left = BinaryTreeNode(5)
        root.left.right = BinaryTreeNode(3)
        root.right.left = BinaryTreeNode(8)
        root.right.right = BinaryTreeNode(9)
        solution = Solution()

        # When
        actual = solution.rob(root)

        # Then
        expected = 83
        self.assertEqual(actual, expected)

    def test_left_child_and_right_grandchildren_included(self):
        # Given
        root = BinaryTreeNode(4)
        root.left = BinaryTreeNode(21)
        root.right = BinaryTreeNode(15)
        root.left.left = BinaryTreeNode(5)
        root.left.right = BinaryTreeNode(10)
        root.right.left = BinaryTreeNode(12)
        root.right.right = BinaryTreeNode(14)
        solution = Solution()

        # When
        actual = solution.rob(root)

        # Then
        expected = 47
        self.assertEqual(actual, expected)
