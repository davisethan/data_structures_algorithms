"""
production algorithm
"""


class Solution:
    def can_partition_array(self, numbers):
        """
        time complexity O(nk)
        space complexity O(nk)
        """
        if sum(numbers) % 2 == 1:
            return False

        k = sum(numbers) // 2
        n = len(numbers)
        memo = [[True if c == 0 else False if m ==
                 0 else None for c in range(k + 1)] for m in range(n + 1)]

        for m in range(1, n + 1):
            for c in range(1, k + 1):
                if numbers[m - 1] <= c:
                    memo[m][c] = memo[m - 1][c - numbers[m - 1]] or \
                        memo[m - 1][c]
                else:
                    memo[m][c] = memo[m - 1][c]

        return memo[n][k]
