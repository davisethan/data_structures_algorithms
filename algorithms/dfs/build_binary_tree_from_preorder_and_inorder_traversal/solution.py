"""
production algorithm
"""

from data_structures.binary_tree.binary_tree import BinaryTreeNode


class Solution:
    def build_tree(self, preorder, inorder):
        """
        time complexity O(n)
        space complexity O(n)
        """
        preorder = preorder[::-1]
        indexer = {inorder[index]: index for index in range(len(inorder))}
        low, high = 0, len(preorder) - 1
        return self.build_tree_helper(preorder, indexer, low, high)

    def build_tree_helper(self, preorder, indexer, low, high):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if high < low:
            return None
        data = preorder.pop()
        mid = indexer[data]
        root = BinaryTreeNode(data)
        root.left = self.build_tree_helper(preorder, indexer, low, mid - 1)
        root.right = self.build_tree_helper(preorder, indexer, mid + 1, high)
        return root
