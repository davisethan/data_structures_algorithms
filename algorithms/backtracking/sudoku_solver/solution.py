"""
production algorithm
"""

DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Solution:
    def solve_sudoku(self, board):
        """
        time complexity O(9^(mn))
        space complexity O(mn)
        """
        n = 9
        row = 0
        column = 0
        visited = self.generate_visited(board, n)
        result = [[]]
        self.solve_sudoku_helper(board, n, row, column, visited, result)
        return result[0]

    def solve_sudoku_helper(self, board, n, row, column, visited, result):
        """
        time complexity O(9^(mn))
        space complexity O(mn)
        """
        if row == n:
            result[0] = [[board[i][j] for j in range(n)] for i in range(n)]
            return

        if column == n:
            self.solve_sudoku_helper(board, n, row + 1, 0, visited, result)
            return

        if board[row][column].isdigit():
            self.solve_sudoku_helper(
                board, n, row, column + 1, visited, result)
            return

        k = n // 3
        rows, columns, grids = visited
        for d in DIGITS:
            if d not in rows[row] and d not in columns[column] and d not in grids[row // k][column // k]:
                # backtracking
                board[row][column] = d
                rows[row].add(d)
                columns[column].add(d)
                grids[row // k][column // k].add(d)
                visited = (rows, columns, grids)
                self.solve_sudoku_helper(
                    board, n, row, column + 1, visited, result)
                board[row][column] = "."
                rows[row].remove(d)
                columns[column].remove(d)
                grids[row // k][column // k].remove(d)

    def generate_visited(self, board, n):
        """
        time complexity O(1)
        space complexity O(1)
        """
        rows = [set() for _ in range(n)]
        for row in range(n):
            for column in range(n):
                if board[row][column].isdigit():
                    rows[row].add(board[row][column])

        columns = [set() for _ in range(n)]
        for column in range(n):
            for row in range(n):
                if board[row][column].isdigit():
                    columns[column].add(board[row][column])

        k = n // 3
        grids = [[set() for _ in range(k)] for _ in range(k)]
        for row in range(n):
            for column in range(n):
                if board[row][column].isdigit():
                    grids[row // k][column // k].add(board[row][column])

        return rows, columns, grids
