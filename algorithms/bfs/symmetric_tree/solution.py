"""
production algorithm
"""

from data_structures.queue.queue import Queue


class Solution:
    def is_symmetric(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        queue = Queue()
        queue.push(root.left)
        queue.push(root.right)
        while not queue.empty():
            left, right = queue.pop(), queue.pop()
            if left and not right or\
                    not left and right or\
                    left and right and not left.data == right.data:
                return False
            if left and right:
                queue.push(left.left)
                queue.push(right.right)
                queue.push(left.right)
                queue.push(right.left)
        return True
