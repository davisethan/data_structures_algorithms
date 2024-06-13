"""
production algorithm
"""


class Solution:
    def longest_common_subsequence(self, s1, s2):
        """
        time complexity O(mn)
        space complexity O(mn)
        """
        k1 = len(s1)
        k2 = len(s2)
        memo = [[0 if m == 0 or n == 0 else None for n in range(
            k2 + 1)] for m in range(k1 + 1)]

        for m in range(1, k1 + 1):
            for n in range(1, k2 + 1):
                if s1[m - 1] == s2[n - 1]:
                    memo[m][n] = 1 + memo[m - 1][n - 1]
                else:
                    memo[m][n] = max(memo[m][n - 1], memo[m - 1][n])

        return memo[k1][k2]
