"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def swap_pairs(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        sentinel = LinkedListNode(None, head)
        current = sentinel
        steps, _, kth_next = self.step_k(sentinel, 2)

        while steps == 2:
            rhead, rtail = self.reverse_k(current.next, 2)
            current.next = rhead
            rtail.next = kth_next
            current = rtail
            steps, _, kth_next = self.step_k(current, 2)

        return sentinel.next

    def step_k(self, head, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        steps = 0
        current = head
        next = head.next
        while steps < k and next:
            steps = steps + 1
            current = next
            next = next.next
        return steps, current, next

    def reverse_k(self, head, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        prev = None
        current = head
        next = head.next
        for _ in range(k):
            current.next = prev
            prev = current
            current = next
            if next:
                next = next.next
        return prev, head
