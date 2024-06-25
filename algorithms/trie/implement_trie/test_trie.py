"""
unit tests
"""

from unittest import TestCase
from algorithms.trie.implement_trie.trie import Trie


class TrieTestCase(TestCase):
    def test_insert(self):
        # Given
        word = "example"
        trie = Trie()

        # When
        trie.insert(word)

        # Then
        current = trie.root
        for character in word:
            self.assertIn(character, current.children)
            current = current.children[character]
        self.assertTrue(current.word)

    def test_search(self):
        # Given
        word = "example"
        trie = Trie()
        trie.insert(word)

        # When
        actual = trie.search(word)

        # Then
        expected = True
        self.assertEqual(actual, expected)

    def test_search_prefix(self):
        # Given
        word = "example"
        prefix = "exam"
        trie = Trie()
        trie.insert(word)

        # When
        actual = trie.search_prefix(prefix)

        # Then
        expected = True
        self.assertEqual(actual, expected)
