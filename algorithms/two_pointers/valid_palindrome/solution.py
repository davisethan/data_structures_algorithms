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
        while low < high:
            if not string[low] == string[high]:
                return False
            low, high = low + 1, high - 1
        return True
