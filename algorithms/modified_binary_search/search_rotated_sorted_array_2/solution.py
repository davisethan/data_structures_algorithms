"""
production algorithm
"""


class Solution:
    def search(self, numbers, target):
        """
        time complexity O(n)
        space complexity O(1)
        """
        low, high = 0, len(numbers) - 1

        while low <= high:
            mid = (high + low) // 2

            if numbers[mid] == target:
                return True

            if numbers[low] == numbers[mid]:
                low += 1
                continue

            # left subarray is in non-descending order
            # otherwise right subarray is in non-descending order
            if numbers[low] < numbers[mid]:

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

        return False
