"""
production algorithm
"""


class Solution:
    def reverse_words(self, sentence):
        """
        time complexity O(n)
        space complexity O(n)
        """
        words = sentence.split()
        low, high = 0, len(words) - 1

        while low < high:
            words[low], words[high] = words[high], words[low]
            low, high = low + 1, high - 1

        return str(" ").join(words)
