"""
production algorithm
"""


class Solution:
    def find_permutations(self, word):
        """
        time complexity O(n * n!)
        space complexity O(n)
        """
        visited, current, result = set(), list(), list()
        self.find_permutations_helper(word, visited, current, result)
        return result

    def find_permutations_helper(self, word, visited, current, result):
        """
        time complexity O(n * n!)
        space complexity O(n)
        """
        if len(current) == len(word):
            result.append(str().join(current))
            return

        for i in range(len(word)):
            if word[i] in visited:
                continue
            visited.add(word[i])
            current.append(word[i])
            self.find_permutations_helper(word, visited, current, result)
            current.pop()
            visited.remove(word[i])
