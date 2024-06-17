"""
production algorithm
"""


class Solution:
    def rotate_image(self, matrix):
        """
        time complexity O(n^2)
        space complexity O(1)
        """
        n = len(matrix)
        for i in range(n - 1):
            for j in range(i, n - 1 - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp
        return matrix
