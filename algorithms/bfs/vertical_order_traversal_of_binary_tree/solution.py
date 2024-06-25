"""
production algorithm
"""

from collections import defaultdict
from data_structures.queue.queue import Queue


class Solution:
    def vertical_order(self, root):
        """
        time complexity O(n)
        space complexity O(n)
        """
        indexer, queue = defaultdict(list), Queue()
        low, high = 0, 0
        queue.push((root, 0))
        while not queue.empty():
            node, column = queue.pop()
            low, high = min(low, column), max(high, column)
            indexer[column].append(node.data)
            if node.left:
                queue.push((node.left, column - 1))
            if node.right:
                queue.push((node.right, column + 1))
        result = [indexer[column] for column in range(low, high + 1)]
        return result
