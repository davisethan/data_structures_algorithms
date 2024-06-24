"""
production algorithm
"""


class Solution:
    def kth_smallest_element(self, root, k):
        """
        time complexity O(n)
        space complexity O(n)
        """
        count, result = [k], []
        self.kth_smallest_element_helper(root, count, result)
        return result[0]

    def kth_smallest_element_helper(self, root, count, result):
        """
        time complexity O(n)
        space complexity O(n)
        """
        if result:
            return
        if root is None:
            return
        self.kth_smallest_element_helper(root.left, count, result)
        count[0] -= 1
        if count[0] == 0:
            result.append(root.data)
        self.kth_smallest_element_helper(root.right, count, result)
