"""
production algorithm
"""


class Solution:
    def verify_alien_dictionary(self, words, order):
        """
        time complexity O(c)
        space complexity O(1)
        """
        indexer = {character: index for index, character in enumerate(order)}

        # iterate consecutive word pairs
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            p, q = len(w1), len(w2)
            d = False

            # iterate length of shortest word in pair
            for j in range(min(p, q)):
                c1, c2 = w1[j], w2[j]
                if not c1 == c2:
                    if indexer[c2] < indexer[c1]:
                        return False
                    d = True
                    break

            if not d and q < p:
                return False

        return True
