"""
production algorithm
"""

from collections import defaultdict


class Solution:
    def right_side_view(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        indexer = defaultdict(int)
        self.right_side_view_helper(root, indexer, 0)
        n = len(indexer)
        return [indexer[i] for i in range(n)]

    def right_side_view_helper(self, root, indexer, n):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if root is None:
            return
        indexer[n] = root.data
        self.right_side_view_helper(root.left, indexer, n + 1)
        self.right_side_view_helper(root.right, indexer, n + 1)
