"""
production algorithm
"""


class Solution:
    def remove_duplicates(self, string):
        """
        time complexity O(n)
        space complexity O(1)
        """
        stack = list()

        for character in string:
            if stack and stack[-1] == character:
                stack.pop()
            else:
                stack.append(character)

        return str().join(stack)
