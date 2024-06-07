"""
production algorithm
"""


class Solution:
    def rescue_boats(self, people, limit):
        """
        time complexity O(nlogn)
        space complexity O(1)
        """
        people.sort()
        low, high = 0, len(people) - 1
        result = 0

        while low <= high:
            if people[low] + people[high] <= limit:
                low = low + 1
            high = high - 1
            result = result + 1

        return result
