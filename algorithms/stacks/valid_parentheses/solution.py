"""
production algorithm
"""

from data_structures.stack.stack import Stack


class Solution:
    def is_valid(self, s):
        """
        time complexity O(n)
        space complexity O(n)
        """
        stack = Stack()

        for c in s:
            if not stack.empty() and \
                (stack.top() == "(" and c == ")") or \
                (stack.top() == "[" and c == "]") or \
                    (stack.top() == "{" and c == "}"):
                stack.pop()
            else:
                stack.push(c)

        return stack.empty()
