"""
production algorithm
"""

from collections import defaultdict


class Solution:
    def find_longest_substring(self, string):
        """
        time complexity O(n)
        space complexity O(1)
        """
        length, low, high = len(string), 0, 0
        frequencies = defaultdict(int)
        result = -1

        for high in range(length):
            frequencies[string[high]] += 1
            while 1 < frequencies[string[high]]:
                frequencies[string[low]] -= 1
                low += 1
            result = max(result, high - low + 1)

        return result
