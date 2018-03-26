# Completely silly exercises, in real life use:
# Python lists: https://docs.python.org/3/tutorial/datastructures.html

import unittest
import logging

logging.basicConfig(level = logging.INFO)


#region Sequential search sort. Best: O(1), average: O(n), worst: O(n). Space: O(1).
def sequential_search(my_value, my_list):
    for index in range(len(my_list)):
        if my_list[index] == my_value:
            return index
    return -1

#endregion


#region TestSearch class.
class TestSearch(unittest.TestCase):
    sut = None

    def setUp(self):
        self.sut = []

    #region Sequential search tests.
    def test_search_empty(self):
        self.assertEqual(sequential_search(1, self.sut), -1)

    def test_search_list(self):
        self.sut = [ 3, 2, 1 ]
        # search_value = 1
        self.assertEqual(sequential_search(1, self.sut), 2)

    def test_search_list_duplicates(self):
        self.sut = [ 3, 1, 2, 2 ]
        # search_value = 1
        self.assertEqual(sequential_search(1, self.sut), 1)
    #endregion

#endregion

if __name__ == "__main__":
    unittest.main(verbosity = 2)