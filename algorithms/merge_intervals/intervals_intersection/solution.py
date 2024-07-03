"""
production algorithm
"""


class Solution:
    def intervals_intersection(self, intervals1, intervals2):
        """
        time complexity O(n + m)
        space complexity O(1)
        """
        index1, index2 = 0, 0
        result = list()

        while index1 < len(intervals1) and index2 < len(intervals2):
            # high of first interval is less than low of second interval
            if intervals1[index1][1] < intervals2[index2][0]:
                index1 = index1 + 1
                continue

            # high of second interval is less than low of first interval
            if intervals2[index2][1] < intervals1[index1][0]:
                index2 = index2 + 1
                continue

            # high of first interval is less than or equal to high of second interval
            if intervals1[index1][1] <= intervals2[index2][1]:
                result.append([max(intervals1[index1][0], intervals2[index2][0]),
                               min(intervals1[index1][1], intervals2[index2][1])])
                index1 = index1 + 1
                continue

            # high of second interval is less than or equal to high of first interval
            result.append([max(intervals1[index1][0], intervals2[index2][0]),
                           min(intervals1[index1][1], intervals2[index2][1])])
            index2 = index2 + 1

        return result
