"""
production algorithm
"""


class Solution:
    def min_remove_parentheses(self, s):
        """
        time complexity O(n)
        space complexity O(n)
        """
        chars = list(s)
        stack = list()

        for i in range(len(chars)):
            if chars[i].isalpha():
                continue
            if stack and chars[stack[-1]] == "(" and chars[i] == ")":
                stack.pop()
            else:
                stack.append(i)

        for i in range(len(chars) - 1, -1, -1):
            if stack and stack[-1] == i:
                chars[i] = str()
                stack.pop()

        return str().join(chars)
