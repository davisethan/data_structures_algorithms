"""
production algorithm
"""


class Solution:
    def merge_intervals(self, intervals):
        """
        time complexity O(n)
        space complexity O(1)
        """
        merged = []
        current = intervals[0]

        for index in range(1, len(intervals)):
            if intervals[index][0] <= current[1]:
                current = [current[0], max(current[1], intervals[index][1])]
            else:
                merged.append(current)
                current = intervals[index]

        merged.append(current)
        return merged
