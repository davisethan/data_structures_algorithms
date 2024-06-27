"""
production algorithm
"""

from collections import Counter


class Solution:
    def first_unique_character(self, s):
        """
        time complexity O(n)
        space complexity O(1)
        """
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
