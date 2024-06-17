"""
production algorithm
"""


class Solution:
    def spiral_order(self, matrix):
        """
        time complexity O(mn)
        space complexity O(1)
        """
        # initialize
        m, n = len(matrix), len(matrix[0])
        lowr, highr, lowc, highc = 0, m, -1, n
        k = m * n
        r, c = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        result = list()

        while len(result) < k:
            # record path
            result.append(matrix[r][c])

            # update direction of path?
            x, y = directions[direction]
            if direction == 0 and c + y == highc:
                highc, direction = highc - 1, (direction + 1) % 4
            if direction == 1 and r + x == highr:
                highr, direction = highr - 1, (direction + 1) % 4
            if direction == 2 and c + y == lowc:
                lowc, direction = lowc + 1, (direction + 1) % 4
            if direction == 3 and r + x == lowr:
                lowr, direction = lowr + 1, (direction + 1) % 4

            # step towards direction
            x, y = directions[direction]
            r, c = r + x, c + y

        return result
