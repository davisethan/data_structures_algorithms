"""
production algorithm
"""

from data_structures.queue.queue import Queue


class Solution:
    def connect_all_siblings(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        queue = Queue()
        queue.push(root)
        while not queue.empty():
            node = queue.pop()
            if node:
                queue.push(node.left)
                queue.push(node.right)
                node.next = queue.peek()
        return root


class CustomBinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
