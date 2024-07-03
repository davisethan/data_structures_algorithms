"""
production algorithm
"""


class Solution:
    def reverse(self, head):
        """
        time complexity O(n)
        space complexity O(1)
        """
        prev = None
        cur = head
        next = cur.next
        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if next:
                next = next.next
        return prev
