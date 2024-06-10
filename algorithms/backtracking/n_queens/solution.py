"""
production algorithm
"""


class Solution:
    def solve_n_queens(self, n):
        """
        time complexity O(n!)
        space complexity O(n)
        """
        row = 0
        columns = {column for column in range(n)}
        main_diagonals = {diagonal for diagonal in range(-n + 1, n)}
        secondary_diagonals = {diagonal for diagonal in range(-n + 1, n)}
        unvisited = (columns, main_diagonals, secondary_diagonals)
        result = [0]
        self.solve_n_queens_helper(n, row, unvisited, result)
        return result[0]

    def solve_n_queens_helper(self, n, row, unvisited, result):
        """
        time complexity O(n!)
        space complexity O(n)
        """
        if row == n:
            result[0] += 1
            return

        columns, main_diagonals, secondary_diagonals = unvisited
        for column in columns.copy():
            main_diagonal = row - column
            secondary_diagonal = n - 1 - row - column
            if main_diagonal in main_diagonals and secondary_diagonal in secondary_diagonals:
                # backtracking
                columns.remove(column)
                main_diagonals.remove(main_diagonal)
                secondary_diagonals.remove(secondary_diagonal)
                unvisited = (columns, main_diagonals, secondary_diagonals)
                self.solve_n_queens_helper(n, row + 1, unvisited, result)
                columns.add(column)
                main_diagonals.add(main_diagonal)
                secondary_diagonals.add(secondary_diagonal)
