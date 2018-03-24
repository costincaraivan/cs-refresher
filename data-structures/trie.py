# Completely silly exercises, in real life use a trie library.

import unittest
import logging

logging.basicConfig(level=logging.INFO)


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("-end")

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "-end" in current:
            return True
        return False

    def starts_with(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True


class TrieTests(unittest.TestCase):

    def setUp(self):
        self.sut = Trie()
        self.sut.insert("abracadabra")
        self.sut.insert("wallalabracadabra")

    def test_search(self):
        self.assertEqual(self.sut.search("abracadabra"), True)

    def test_starts_with_ok(self):
        self.assertEqual(self.sut.starts_with("abra"), True)

    def test_starts_with_fails(self):
        self.assertEqual(self.sut.starts_with("zzzz"), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)