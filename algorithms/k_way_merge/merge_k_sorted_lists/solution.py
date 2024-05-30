"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedList, LinkedListNode
from data_structures.heap.heap import Heap


class Solution:
    def merge_k_lists(self, lists):
        """
        time complexity O(nlogk)
        space complexity O(k)
        """
        smallest = Heap()
        [smallest.push(MinHeapData(lists[i].head.next))
         for i in range(len(lists)) if lists[i].head.next]
        sentinel = LinkedListNode(None)
        cur = sentinel

        while not smallest.empty():
            node = smallest.pop().node
            cur.next, cur = node, node
            if node and node.next:
                smallest.push(MinHeapData(node.next))

        return LinkedList(sentinel)


class MinHeapData:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.data < other.node.data
