"""
unit tests
"""

from unittest import TestCase
from algorithms.bfs.connect_all_siblings_of_binary_tree.solution import Solution, CustomBinaryTreeNode


class SolutionTestCase(TestCase):
    def test_connect_all_siblings(self):
        # Given
        root = CustomBinaryTreeNode(-6)
        root.left = CustomBinaryTreeNode(-15)
        root.right = CustomBinaryTreeNode(7)
        root.left.left = CustomBinaryTreeNode(-18)
        root.left.right = CustomBinaryTreeNode(-11)
        root.right.left = CustomBinaryTreeNode(1)
        root.right.right = CustomBinaryTreeNode(17)
        root.left.left.left = CustomBinaryTreeNode(-19)
        root.left.left.right = CustomBinaryTreeNode(-17)
        root.left.right.left = CustomBinaryTreeNode(-12)
        root.left.right.right = CustomBinaryTreeNode(-8)
        root.right.left.left = CustomBinaryTreeNode(-5)
        root.right.left.right = CustomBinaryTreeNode(6)
        root.right.right.left = CustomBinaryTreeNode(13)
        root.right.right.right = CustomBinaryTreeNode(20)
        solution = Solution()

        # When
        result = solution.connect_all_siblings(root)

        # Then
        numbers = [-6, -15, 7, -18, -11, 1,
                   17, -19, -17, -12, -8, -5, 6, 13, 20]
        current = result
        for number in numbers:
            self.assertEqual(current.data, number)
            current = current.next
        self.assertEqual(current, None)
