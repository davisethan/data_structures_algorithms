"""
production algorithm
"""

from collections import Counter


class Solution:
    def is_anagram(self, str1, str2):
        """
        time complexity O(n)
        space complexity O(1)
        """
        counter1, counter2 = Counter(str1), Counter(str2)

        for character in counter1:
            if not counter1.get(character) == counter2.get(character):
                return False
        for character in counter2:
            if not counter2.get(character) == counter1.get(character):
                return False

        return True
