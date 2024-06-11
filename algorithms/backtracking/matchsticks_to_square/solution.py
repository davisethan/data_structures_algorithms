"""
production algorithm
"""


class Solution:
    def matchsticks_to_square(self, matchsticks):
        """
        time complexity O(4^n)
        space complexity O(n)
        """
        n, i = len(matchsticks), 0
        visited = [0, 0, 0, 0]
        k = len(visited)
        result = [False]
        self.matchsticks_to_square_helper(
            matchsticks, n, i, visited, k, result)
        return result[0]

    def matchsticks_to_square_helper(self, matchsticks, n, i, visited, k, result):
        """
        time complexity O(4^n)
        space complexity O(n)
        """
        if i == n:
            if visited[0] == visited[1] == visited[2] == visited[3]:
                result[0] = True
            return

        for j in range(k):
            visited[j] += matchsticks[i]
            self.matchsticks_to_square_helper(
                matchsticks, n, i + 1, visited, k, result)
            visited[j] -= matchsticks[i]
