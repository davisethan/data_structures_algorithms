"""
production algorithm
"""


class Solution:
    def letter_combinations(self, digits):
        """
        time complexity O(n * k^n)
        space complexity O(nk)
        """
        if len(digits) == 0:
            return list()
        words = self.generate_words(digits)
        n, i = len(words), 0
        current, result = list(), list()
        self.letter_combinations_helper(words, n, i, current, result)
        return result

    def letter_combinations_helper(self, words, n, i, current, result):
        """
        time complexity O(n * k^n)
        space complexity O(n)
        """
        if i == n:
            result.append(str().join(current))
            return
        for character in words[i]:
            current.append(character)
            self.letter_combinations_helper(words, n, i + 1, current, result)
            current.pop()

    def generate_words(self, digits):
        """
        time complexity O(n)
        space complexity O(nk)
        """
        map = [None, None, "abc", "def", "ghi",
               "jkl", "mno", "pqrs", "tuv", "wxyz"]
        words = [map[int(d)] for d in digits]
        return words
