"""
production algorithm
"""


class Solution:
    def mirror_binary_tree(self, root):
        """
        time complexity XXX
        space complexity XXX
        """
        self.mirror_binary_tree_helper(root)
        return root

    def mirror_binary_tree_helper(self, root):
        """
        time complexity XXX
        space complexity XXX
        """
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.mirror_binary_tree_helper(root.left)
        self.mirror_binary_tree_helper(root.right)
