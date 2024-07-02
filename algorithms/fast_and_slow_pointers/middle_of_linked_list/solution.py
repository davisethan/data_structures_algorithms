"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def get_middle_node(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        sentinel = LinkedListNode(None, head)
        slow, fast = sentinel.next, sentinel.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if not fast:
            return slow
        return slow.next
