"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def detect_cycle(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        sentinel = LinkedListNode(None, head)
        if not sentinel.next or not sentinel.next.next:
            return False
        slow, fast = sentinel.next, sentinel.next.next

        while not slow == fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow == fast
