"""
production algorithm
"""


class Solution:
    def single_non_duplicate(self, numbers):
        """
        time complexity O(logn)
        spae complexity O(1)
        """
        low, high = 0, len(numbers) - 1

        while low < high:
            mid = (low + high) // 2

            if mid % 2 == 1:
                mid = mid - 1

            if numbers[mid] == numbers[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return numbers[low]
