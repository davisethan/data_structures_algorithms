"""
production algorithm
"""


class Solution:
    def binary_search(self, nums, target):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1
