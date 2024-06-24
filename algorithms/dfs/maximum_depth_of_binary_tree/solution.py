"""
production algorithm
"""


class Solution:
    def find_max_depth(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        return self.find_max_depth_helper(root)

    def find_max_depth_helper(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if root is None:
            return 0
        return 1 + max(self.find_max_depth_helper(root.left), self.find_max_depth_helper(root.right))
