"""
production algorithm
"""


class Solution:
    def find_permutations(self, word):
        """
        time complexity O(n * n!)
        space complexity O(n)
        """
        current, result = str(), list()
        self.find_permutations_helper(word, current, result)
        return result

    def find_permutations_helper(self, word, current, result):
        """
        time complexity O(n * n!)
        space complexity O(n)
        """
        if len(word) == 0:
            result.append(current)
        for i in range(len(word)):
            self.find_permutations_helper(
                word[:i] + word[i+1:], current + word[i], result)
