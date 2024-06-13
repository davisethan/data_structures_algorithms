"""
production algorithm
"""


class Solution:
    def count_palindromic_substrings(self, s):
        """
        time complexity O(n^2)
        space complexity O(n^2)
        """
        n = len(s)
        memo = [[True if i == j else None for j in range(n)] for i in range(n)]
        count = n

        for m in range(1, n):
            for k in range(0, n - m):
                if m == 1:
                    memo[k][k + m] = s[k] == s[k + m]
                else:
                    memo[k][k + m] = s[k] == s[k + m] and \
                        memo[k + 1][k + m - 1]
                if memo[k][k + m]:
                    count += 1

        return count
