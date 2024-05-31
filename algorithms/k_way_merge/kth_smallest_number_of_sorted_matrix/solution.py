"""
production algorithm
"""

from algorithms.k_way_merge.kth_smallest_number.solution import Solution as Solution2


class Solution:
    def kth_smallest_number(self, matrix, k):
        solution2 = Solution2()
        return solution2.k_smallest_number(matrix, k)
