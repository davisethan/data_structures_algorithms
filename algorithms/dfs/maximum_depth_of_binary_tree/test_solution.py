"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.maximum_depth_of_binary_tree.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_maximum_depth_is_zero(self):
        # Given
        root = None
        solution = Solution()

        # When
        actual = solution.find_max_depth(root)

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_maximum_depth_is_one(self):
        # Given
        root = BinaryTreeNode(0)
        solution = Solution()

        # When
        actual = solution.find_max_depth(root)

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_maximum_depth_is_five(self):
        # Given
        root = BinaryTreeNode(0)
        root.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(4)
        root.left.right.left = BinaryTreeNode(6)
        root.left.right.left.right = BinaryTreeNode(8)
        solution = Solution()

        # When
        actual = solution.find_max_depth(root)

        # Then
        expected = 5
        self.assertEqual(actual, expected)
