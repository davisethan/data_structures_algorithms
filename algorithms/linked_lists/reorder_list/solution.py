"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def reorder_list(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        if head.next is None or head.next.next is None:
            return head

        sentinel = LinkedListNode(None, head)
        mid_prev, mid = self.middle(sentinel)
        mid_prev.next = None
        mid = self.reverse(mid)
        return self.merge(head, mid)

    def middle(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        low_prev = None
        low = head
        high = head
        while high:
            low_prev = low
            low = low.next
            high = high.next
            if high:
                high = high.next
        return low_prev, low

    def reverse(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        prev = None
        cur = head
        next = head.next
        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if next:
                next = next.next
        return prev

    def merge(self, head1, head2):
        """
        time complexity O(n)
        space complexity O(1)
        """
        low = head1
        low_next = head1.next
        high = head2
        high_next = head2.next
        while low_next:
            low.next = high
            high.next = low_next
            low = low_next
            low_next = low_next.next
            high = high_next
            high_next = high_next.next
        low.next = high
        return head1
