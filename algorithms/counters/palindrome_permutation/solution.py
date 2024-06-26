"""
production algorithm
"""

from collections import Counter


class Solution:
    def permute_palindrome(self, s):
        """
        time complexity O(n)
        space complexity O(1)
        """
        counter, count = Counter(s), 0
        for character in counter:
            if counter[character] % 2 == 1:
                count += 1
        return count < 2
