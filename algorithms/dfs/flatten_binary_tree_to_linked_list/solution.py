"""
production algorithm
"""

class Solution:
    def flatten_tree(self, root):
        """
        time complexity O(n)
        space complexity O(1)
        """
        current = root
        while current:
            if current.left:
                last = current.left
                while last.right:
                    last = last.right
                last.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
        return root
