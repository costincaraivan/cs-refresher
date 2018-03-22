# Completely silly exercises, in real life use a trie library.

import unittest
import logging

logging.basicConfig(level=logging.INFO)


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

    def __str__(self):
        return "{} {} {} {}".format(self.char,
                                    str([x.char for x in self.children]),
                                    self.word_finished, self.counter)


class Trie:
    def __init__(self, root):
        self.root = root

    def add(self, word):
        for char in word:
            found_in_child = False
            for child in self.root.children:
                if child.char == char:
                    child.counter += 1
                    self.root = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                self.root.children.append(new_node)
        self.root.word_finished = True


class TrieTests(unittest.TestCase):
    sut = None

    def setUp(self):
        root_node = TrieNode("*")
        self.sut = Trie(root_node)

    def test_search(self):
        logging.info(self.sut.root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
