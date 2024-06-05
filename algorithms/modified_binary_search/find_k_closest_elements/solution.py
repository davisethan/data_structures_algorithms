"""
production algorithm
"""


class Solution:
    def find_closest_elements(self, numbers, target, k):
        """
        time complexity O(n)
        space complexity O(1)
        """
        # find nearest
        nearest = self.binary_search_nearest(numbers, target)
        low, high = nearest, nearest

        # find k nearest
        while high - low + 1 < k:
            if low - 1 < 0:
                high += 1
                continue
            if high + 1 > len(numbers) - 1:
                low -= 1
                continue
            if abs(numbers[low - 1] - target) <= abs(numbers[high + 1] - target):
                low -= 1
            else:
                high += 1

        return numbers[low:high+1]

    def binary_search_nearest(self, numbers, target):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        low, high = 0, len(numbers) - 1

        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == target:
                return mid
            if numbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if len(numbers) <= low:
            return high
        if high < 0:
            return low
        if abs(numbers[low] - target) < abs(numbers[high] - target):
            return low
        else:
            return high
