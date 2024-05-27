"""
production algorithm
"""


class Solution:
    def find_repeated_sequences(self, string, length):
        if len(string) < length:
            return set()

        # build rolling hash
        indexer = {"A": 1, "C": 2, "G": 3, "T": 4}
        base1, modulo1 = 31, 10 ** 9 + 7
        base2, modulo2 = 37, 10 ** 9 + 9
        hash1 = sum([indexer[string[index]] * base1 ** (length - 1 - index)
                    for index in range(length)]) % modulo1
        hash2 = sum([indexer[string[index]] * base2 ** (length - 1 - index)
                    for index in range(length)]) % modulo2
        visited, result = set(), set()
        visited.add((hash1, hash2))

        # step rolling hash
        for index in range(length, len(string)):
            hash1 = ((hash1 - indexer[string[index - length]] * base1 **
                     (length - 1)) * base1 + indexer[string[index]]) % modulo1
            hash2 = ((hash2 - indexer[string[index - length]] * base2 **
                     (length - 1)) * base2 + indexer[string[index]]) % modulo2
            if (hash1, hash2) in visited:
                substring = string[index - length + 1: index + 1]
                result.add(substring)
            visited.add((hash1, hash2))

        return result
