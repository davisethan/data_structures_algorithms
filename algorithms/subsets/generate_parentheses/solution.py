"""
production algorithm
"""


class Solution:
    def generate_combinations(self, n):
        """
        time complexity O(n * 4^n)
        space complexity O(n)
        """
        opened, closed = n, n
        current, result = list(), list()
        self.generate_combinations_helper(opened, closed, current, result)
        return result

    def generate_combinations_helper(self, opened, closed, current, result):
        """
        time complexity O(n * 4^n)
        space complexity O(n)
        """
        # generated more closed than opened parentheses
        if closed < opened:
            return

        # generated more opened parentheses than is valid
        if opened < 0:
            return

        # generated balanced combination of opened and closed parentheses
        if opened == 0 and closed == 0:
            result.append(str().join(current))
            return

        current.append("(")
        self.generate_combinations_helper(opened - 1, closed, current, result)
        current.pop()

        current.append(")")
        self.generate_combinations_helper(opened, closed - 1, current, result)
        current.pop()
