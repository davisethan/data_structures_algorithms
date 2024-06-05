"""
production algorithm
"""


class Solution:
    def binary_search_rotated(self, numbers, target):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        low, high = 0, len(numbers) - 1

        while low <= high:
            mid = (high + low) // 2

            if numbers[mid] == target:
                return mid

            # left subarray is strictly increasing
            # otherwise right subarray is strictly increasing
            if numbers[low] <= numbers[mid]:

                # target would be in left subarray
                # otherwise target would be in right subarray
                if numbers[low] <= target < numbers[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:

                # target would be in right subarray
                # otherwise target would be in left subarray
                if numbers[mid] < target <= numbers[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
