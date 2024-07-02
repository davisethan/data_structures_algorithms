"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedListNode


class Solution:
    def palindrome(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        middle = self.middle(head)
        middle = self.reverse(middle)
        is_palindrome = self.palindrome_helper(head, middle)
        self.reverse(middle)
        return is_palindrome

    def middle(self, head):
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

    def reverse(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        prev, cur, next = None, head, head.next

        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if next:
                next = next.next

        return prev

    def palindrome_helper(self, head1, head2):
        """
        time complexity O(n)
        space complexity O(1)
        """
        current1, current2 = head1, head2

        while current2 and current1.data == current2.data:
            current1, current2 = current1.next, current2.next

        if not current2:
            return True
        return False
