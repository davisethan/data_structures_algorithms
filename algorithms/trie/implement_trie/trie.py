"""
production algorithm
"""


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        time complexity O(n)
        space complexity O(1)
        """
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.word = True

    def search(self, word):
        """
        time complexity O(n)
        space complexity O(1)
        """
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.word

    def search_prefix(self, prefix):
        """
        time complexity O(n)
        space complexity O(1)
        """
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False
