"""
unit tests
"""

from unittest import TestCase
from algorithms.dfs.kth_smallest_element_in_bst.solution import Solution
from data_structures.binary_tree.binary_tree import BinaryTreeNode


class SolutionTestCase(TestCase):
    def test_0th_smallest_element(self):
        # Given
        root = BinaryTreeNode(9)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(11)
        root.left.left = BinaryTreeNode(-1)
        root.left.right = BinaryTreeNode(6)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(16)
        root.right.right.right = BinaryTreeNode(18)
        k = 1
        solution = Solution()

        # When
        actual = solution.kth_smallest_element(root, k)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_kth_smallest_element(self):
        # Given
        root = BinaryTreeNode(9)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(11)
        root.left.left = BinaryTreeNode(-1)
        root.left.right = BinaryTreeNode(6)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(16)
        root.right.right.right = BinaryTreeNode(18)
        k = 5
        solution = Solution()

        # When
        actual = solution.kth_smallest_element(root, k)

        # Then
        expected = 10
        self.assertEqual(actual, expected)

    def test_nth_smallest_element(self):
        # Given
        root = BinaryTreeNode(9)
        root.left = BinaryTreeNode(3)
        root.right = BinaryTreeNode(11)
        root.left.left = BinaryTreeNode(-1)
        root.left.right = BinaryTreeNode(6)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(16)
        root.right.right.right = BinaryTreeNode(18)
        k = 8
        solution = Solution()

        # When
        actual = solution.kth_smallest_element(root, k)

        # Then
        expected = 18
        self.assertEqual(actual, expected)
