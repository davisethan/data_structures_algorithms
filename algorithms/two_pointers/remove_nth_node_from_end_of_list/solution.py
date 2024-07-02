"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def remove_nth_last_node(self, head, n):
        """
        time complexity O(n)
        space complexity O(1)
        """
        sentinel = LinkedListNode(None, head)
        nth_last_prev, _, nth_last_next = self.nth_last_node(sentinel, n)
        nth_last_prev.next = nth_last_next
        return sentinel.next

    def nth_last_node(self, head, n):
        """
        time complexity O(n)
        space complexity O(1)
        """
        low_prev, low, low_next = None, head, head.next
        high = head

        for _ in range(n):
            high = high.next

        while high is not None:
            low_prev, low, low_next = low, low_next, low_next.next
            high = high.next

        return low_prev, low, low_next
