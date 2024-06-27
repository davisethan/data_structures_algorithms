"""
production algorithm
"""

from collections import Counter


class Solution:
    def can_construct(self, note, magazine):
        """
        time complexity O(n + m)
        space complexity O(1)
        """
        counter = Counter(magazine)
        for char in note:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        return True
