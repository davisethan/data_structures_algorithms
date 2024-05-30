"""
production algorithm
"""


class Solution:
    def merge_sorted(self, nums1, m, nums2, n):
        """
        time complexity O(n)
        space complexity O(1)
        """
        i, j, k = m - 1, n - 1, m + n - 1

        # reverse iteration of both arrays
        while 0 <= i and 0 <= j:
            if nums2[j] < nums1[i]:
                nums1[k], i, k = nums1[i], i - 1, k - 1
            else:
                nums1[k], j, k = nums2[j], j - 1, k - 1

        # reverse iteration remainder of first array
        while 0 <= i:
            nums1[k], i, k = nums1[i], i - 1, k - 1

        # reverse iteration remainder of second array
        while 0 <= j:
            nums1[k], j, k = nums2[j], j - 1, k - 1

        return nums1
