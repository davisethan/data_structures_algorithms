"""
production algorithm
"""

from algorithms.two_heaps.schedule_tasks_on_minimum_machines.solution import Solution as Solution2


class Solution:
    def find_rooms(self, intervals):
        """
        time complexity O(nlogn)
        space complexity O(n)
        """
        solution2 = Solution2()
        return solution2.minimum_machines(intervals)
