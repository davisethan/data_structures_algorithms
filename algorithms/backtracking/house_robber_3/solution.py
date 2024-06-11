"""
production algorithm
"""


class Solution:
    def rob(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        return max(self.rob_helper(root))

    def rob_helper(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if root is None:
            return 0, 0

        left_root_included, left_root_excluded = self.rob_helper(root.left)
        right_root_included, right_root_excluded = self.rob_helper(root.right)
        root_included = root.data + left_root_excluded + right_root_excluded
        root_excluded = max(left_root_included, left_root_excluded) + \
            max(right_root_included, right_root_excluded)

        return root_included, root_excluded
