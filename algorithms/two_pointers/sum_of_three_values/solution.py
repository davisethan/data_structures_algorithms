"""
production algorithm
"""


class Solution:
    def find_sum_of_three(self, numbers, target):
        """
        time complexity O(n^2)
        space complexity O(1)
        """
        numbers.sort()
        size = len(numbers)
        for lowest in range(size - 2):
            low, high = lowest + 1, size - 1
            while low < high:
                sum = numbers[lowest] + numbers[low] + numbers[high]
                if sum == target:
                    return True
                if sum < target:
                    low += 1
                else:
                    high -= 1
        return False
