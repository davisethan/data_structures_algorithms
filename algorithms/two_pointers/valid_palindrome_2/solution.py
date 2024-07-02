"""
production algorithm
"""


class Solution:
    def is_palindrome(self, string):
        """
        time complexity O(n)
        space complexity O(1)
        """
        low, high = 0, len(string) - 1
        removed = 0
        return self.is_palindrome_helper(string, low, high, removed)

    def is_palindrome_helper(self, string, low, high, removed):
        """
        time complexity O(n)
        space complexity O(1)
        """
        while low < high:
            if not string[low] == string[high]:
                if 0 < removed:
                    return False
                if self.is_palindrome_helper(string, low + 1, high, removed + 1):
                    return True
                if self.is_palindrome_helper(string, low, high - 1, removed + 1):
                    return True
                return False
            low, high = low + 1, high - 1
        return True
