"""
production algorithm
"""


class Solution:
    def minimum_size_subarray_sum(self, numbers, target):
        length, low, high = len(numbers), 0, 0
        current = 0
        result = float("inf")

        # step forward high index
        for high in range(length):
            current += numbers[high]

            # step forward low index
            while target <= current:
                result = min(result, high - low + 1)
                current -= numbers[low]
                low += 1

        if result == float("inf"):
            return 0
        return result
