"""
production algorithm
"""

from data_structures.binary_tree.binary_tree import BinaryTreeNode


class Solution:
    def serialize(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        stream = list()
        self.serialize_helper(root, stream)
        return stream

    def serialize_helper(self, root, stream):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if not root:
            stream.append(None)
            return
        stream.append(root.data)
        self.serialize_helper(root.left, stream)
        self.serialize_helper(root.right, stream)

    def deserialize(self, stream):
        """
        time complexity O(n)
        space complexity O(n)
        """
        stream = stream[::-1]
        return self.deserialize_helper(stream)

    def deserialize_helper(self, stream):
        """
        time complexity O(n)
        space complexity O(n)
        """
        data = stream.pop()
        if data is None:
            return None
        root = BinaryTreeNode(data)
        root.left = self.deserialize_helper(stream)
        root.right = self.deserialize_helper(stream)
        return root
