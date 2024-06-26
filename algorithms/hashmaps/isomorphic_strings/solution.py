"""
production algorithm
"""

from collections import defaultdict


class Solution:
    def is_isomorphic(self, s1, s2):
        """
        time complexity O(n)
        space complexity O(1)
        """
        n = len(s1)
        hashmap1, hashmap2 = defaultdict(int), defaultdict(int)
        for i in range(n):
            hashmap1[s1[i]] += 1
            hashmap2[s2[i]] += 1
            if not hashmap1[s1[i]] == hashmap2[s2[i]]:
                return False
        return True
