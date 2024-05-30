"""
production algorithm
"""

from data_structures.linked_list.linked_list import LinkedList, LinkedListNode


class Solution:
    def merge_k_lists(self, lists):
        """
        time complexity O(nlogk)
        space complexity O(n)
        """
        if len(lists) == 0:
            return None
        return self.merge_k_lists_helper(lists)

    def merge_k_lists_helper(self, lists):
        """
        time complexity O(nlogk)
        space complexity O(n)
        """
        if len(lists) == 1:
            return lists[0]
        return self.merge(
            self.merge_k_lists_helper(lists[:len(lists) // 2]),
            self.merge_k_lists_helper(lists[len(lists) // 2:]))

    def merge(self, list1, list2):
        """
        time complexity O(n)
        space complexity O(1)
        """
        sentinel = LinkedListNode()
        cur, cur1, cur2 = sentinel, list1.head.next, list2.head.next

        while cur1 and cur2:
            if cur1.data < cur2.data:
                cur.next, cur, cur1 = cur1, cur1, cur1.next
            else:
                cur.next, cur, cur2 = cur2, cur2, cur2.next

        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2

        return LinkedList(sentinel)
