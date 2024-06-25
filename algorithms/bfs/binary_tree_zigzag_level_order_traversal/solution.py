"""
production algorithm
"""

from collections import deque


class Solution:
    def zigzag_level_order(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if root is None:
            return list()
        current, next, result = deque(), deque(), list()
        next.append(root)
        # next level exists
        while next:
            current, next = next, deque()
            result.append(list())
            # next element of level exists
            while current:
                # pop from left to right
                if len(result) % 2 == 1:
                    node = current.popleft()
                    result[-1].append(node.data)
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
                # pop from right to left
                else:
                    node = current.pop()
                    result[-1].append(node.data)
                    if node.right:
                        next.appendleft(node.right)
                    if node.left:
                        next.appendleft(node.left)
        return result
