"""
production algorithm
"""


class Solution:
    def diameter_of_binary_tree(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        _, diameter = self.diameter_of_binary_tree_helper(root)
        return diameter

    def diameter_of_binary_tree_helper(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if root is None:
            return -1, 0
        lheight, ldiameter = self.diameter_of_binary_tree_helper(root.left)
        rheight, rdiameter = self.diameter_of_binary_tree_helper(root.right)
        return 1 + max(lheight, rheight), max(2 + lheight + rheight, ldiameter, rdiameter)
