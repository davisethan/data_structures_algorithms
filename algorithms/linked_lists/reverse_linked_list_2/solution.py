"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def reverse_between(self, head, left, right):
        """
        time complexity O(n)
        space complexity O(1)
        """
        sentinel = LinkedListNode(None, head)

        left_prev = self.kth_node(sentinel, left - 1)
        left_node = self.kth_node(sentinel, left)
        right_next = self.kth_node(sentinel, right + 1)

        head_node, tail_node = self.reverse_k(left_node, right - left + 1)

        left_prev.next = head_node
        tail_node.next = right_next

        return sentinel.next

    def kth_node(self, head, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        cur = head
        for _ in range(k):
            cur = cur.next
        return cur

    def reverse_k(self, head, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        prev = None
        cur = head
        next = head.next
        for _ in range(k):
            cur.next = prev
            prev = cur
            cur = next
            if next:
                next = next.next
        return prev, head
