"""
production algorithm
"""

from collections import Counter


class Solution:
    def longest_palindrome(self, s):
        """
        time complexity O(n)
        space complexity O(1)
        """
        counter = Counter(s)
        odds, evens = 0, 0

        for character in counter:
            if counter[character] % 2 == 0:
                evens += counter[character]
            else:
                odds += 1
                evens += counter[character] - 1

        if 0 < odds:
            return evens + 1
        return evens
