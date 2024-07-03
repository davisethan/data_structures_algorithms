"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def swap_nodes(self, head, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        sentinel = LinkedListNode(None, head)
        kth_prev, kth, kth_next = self.kth_node(sentinel, k)
        kth_last_prev, kth_last, kth_last_next = self.kth_last_node(
            sentinel, k)

        if kth == kth_last:
            return sentinel.next
        if kth.next == kth_last:
            kth_prev.next = kth_last
            kth.next = kth_last_next
            kth_last.next = kth
            return sentinel.next
        kth_prev.next = kth_last
        kth.next = kth_last_next
        kth_last.next = kth_next
        kth_last_prev.next = kth
        return sentinel.next

    def kth_node(self, head, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        prev = None
        cur = head
        next = head.next
        for _ in range(k):
            prev = cur
            cur = next
            next = next.next
        return prev, cur, next

    def kth_last_node(self, head, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        low_prev = None
        low = head
        low_next = head.next
        _, high, _ = self.kth_node(head, k)
        while high:
            low_prev = low
            low = low_next
            low_next = low_next.next
            high = high.next
        return low_prev, low, low_next
