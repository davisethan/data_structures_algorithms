"""
production algorithm
"""

from data_structures.queue.queue import Queue


class Solution:
    def clone(self, root):
        """
        time complexity O(V + E)
        space complexity O(V)
        """
        copy = dict()
        queue = Queue()
        queue.push(root)
        while not queue.empty():
            node = queue.pop()
            if node.data not in copy:
                copy[node.data] = Node(node.data)
            for neighbor in node.neighbors:
                if neighbor.data not in copy:
                    copy[neighbor.data] = Node(neighbor.data)
                    queue.push(neighbor)
                copy[node.data].neighbors.append(copy[neighbor.data])
        return copy[root.data]


class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def __eq__(self, other):
        data = self.data == other.data
        length = len(self.neighbors) == len(other.neighbors)
        neighbors = all([self.neighbors[i].data ==
                        other.neighbors[i].data for i in range(len(self.neighbors))])
        return data and length and neighbors

    def __repr__(self):
        return str(self.data)
