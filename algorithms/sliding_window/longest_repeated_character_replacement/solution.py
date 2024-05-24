"""
production algorithm
"""

from collections import defaultdict


class Solution:
    def longest_repeated_character_replacement(self, string, capacity):
        length, low, high = len(string), 0, 0
        max_frequency, frequencies = -1, defaultdict(int)

        for high in range(length):
            frequencies[string[high]] = frequencies[string[high]] + 1
            max_frequency = max(max_frequency, frequencies[string[high]])
            if capacity < high - low + 1 - max_frequency:
                frequencies[string[low]] = frequencies[string[low]] - 1
                low = low + 1

        return high - low + 1
