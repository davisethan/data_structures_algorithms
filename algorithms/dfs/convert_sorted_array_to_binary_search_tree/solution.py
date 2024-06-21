"""
production algorithm
"""

from data_structures.binary_tree.binary_tree import BinaryTreeNode


class Solution:
    def sorted_array_to_bst(self, numbers):
        """
        time complexity O(n)
        space complexity O(logn)
        """
        low, high = 0, len(numbers) - 1
        return self.sorted_array_to_bst_helper(numbers, low, high)

    def sorted_array_to_bst_helper(self, numbers, low, high):
        """
        time complexity O(n)
        space complexity O(logn)
        """
        if high < low:
            return None
        mid = low + (high - low) // 2
        root = BinaryTreeNode(numbers[mid])
        root.left = self.sorted_array_to_bst_helper(numbers, low, mid - 1)
        root.right = self.sorted_array_to_bst_helper(numbers, mid + 1, high)
        return root
