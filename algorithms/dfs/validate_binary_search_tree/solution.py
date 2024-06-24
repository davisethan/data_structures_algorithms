"""
production algorithm
"""


class Solution:
    def validate_bst(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        prev, result = [float("-inf")], [True]
        self.validate_bst_helper(root, prev, result)
        return result[0]

    def validate_bst_helper(self, root, prev, result):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if root is None:
            return
        self.validate_bst_helper(root.left, prev, result)
        result[0], prev[0] = result[0] and prev[0] < root.data, root.data
        self.validate_bst_helper(root.right, prev, result)
