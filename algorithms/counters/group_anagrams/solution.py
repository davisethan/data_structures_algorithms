"""
production algorithm
"""

from collections import defaultdict


class Solution:
    def group_anagrams(self, strings):
        """
        time complexity O(nk)
        space complexity O(nk)
        """
        anagrams = defaultdict(list)

        for string in strings:
            # find frequencies of characters
            frequencies = [0 for _ in range(26)]
            for character in string:
                frequencies[ord(character) - ord("a")] += 1

            # group strings by frequencies of characters
            anagrams[tuple(frequencies)].append(string)

        return anagrams.values()
