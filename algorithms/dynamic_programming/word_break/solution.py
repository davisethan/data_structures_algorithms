"""
production algorithm
"""


class Solution:
    def word_break(self, string, dictionary):
        """
        time complexity O(n^3)
        space complexity O(n)
        """
        n = len(string)
        memo = [True if k == 0 else None for k in range(n + 1)]

        for k in range(1, n + 1):
            memo[k] = False
            for i in range(k):
                if string[i:k] in dictionary and memo[i]:
                    memo[k] = True

        return memo[n]
