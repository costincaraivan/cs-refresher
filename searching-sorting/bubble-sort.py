# Completely silly exercises, in real life use:
# Python lists: https://docs.python.org/3/tutorial/datastructures.html

import unittest
import logging

logging.basicConfig(level = logging.INFO)

#region Bubble sort. Best: O(n), average: O(n^2), worst: O(n^2). Space: 1 (or even 0 :) ). Stable.
def bubble_sort(my_list):
    for number_passes in range(len(my_list) - 1, 0, -1):
        for index in range(number_passes):
            if my_list[index] > my_list[index + 1]:
                my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
#endregion

#region Insertion sort. Best: O(n), average: O(n^2), worst: O(n^2). Space: 1. Stable.
def insertion_sort(my_list):
    for index in range(1, len(my_list)):        
        current_value = my_list[index]
        position = index

        while position > 0 and my_list[position - 1] > current_value:
            my_list[position] = my_list[position - 1]
            position = position - 1

        my_list[position] = current_value
#endregion

#region Selection sort. Best: O(n), average: O(n^2), worst: O(n^2). Space: 1. Stable.
def selection_sort(my_list):
    if my_list == None or my_list == []:
        return
    for slot in range(len(my_list) - 1, 0, -1):
        max_position = 0
        for index in range(1, slot + 1):
            if my_list[index] > my_list[max_position]:
                max_position = index
        my_list[slot], my_list[max_position] = my_list[max_position], my_list[slot]
#endregion

#region TestSort class.
class TestSort(unittest.TestCase):
    sut = None

    def setUp(self):
        self.sut = []

    #region Bubble sort tests.
    def test_bubble_sort_empty(self):
        expected_list = []
        bubble_sort(self.sut)     
        self.assertEqual(self.sut, expected_list)

    def test_bubble_sort_sorted(self):
        self.sut = [ 1, 2, 3 ]
        expected_list = [ 1, 2, 3 ]
        bubble_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

    def test_bubble_sort_unsorted(self):
        self.sut = [ 3, 1, 2 ]
        expected_list = [ 1, 2, 3 ]
        bubble_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

    def test_bubble_sort_duplicates(self):
        self.sut = [ 3, 1, 2, 2 ]
        expected_list = [ 1, 2, 2, 3 ]
        bubble_sort(self.sut)
        self.assertEqual(self.sut, expected_list)
    #endregion

    #region Insert sort tests.
    def test_insertion_sort_empty(self):
        expected_list = []
        insertion_sort(self.sut)     
        self.assertEqual(self.sut, expected_list)

    def test_insertion_sort_sorted(self):
        self.sut = [ 1, 2, 3 ]
        expected_list = [ 1, 2, 3 ]
        insertion_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

    def test_insertion_sort_unsorted(self):
        self.sut = [ 3, 1, 2 ]
        expected_list = [ 1, 2, 3 ]
        insertion_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

    def test_insertion_sort_duplicates(self):
        self.sut = [ 3, 1, 2, 2 ]
        expected_list = [ 1, 2, 2, 3 ]
        insertion_sort(self.sut)
        self.assertEqual(self.sut, expected_list)
    #endregion

    #region Selection sort tests.
    def test_selection_sort_empty(self):
        expected_list = []
        selection_sort(self.sut)     
        self.assertEqual(self.sut, expected_list)

    def test_selection_sort_sorted(self):
        self.sut = [ 1, 2, 3 ]
        expected_list = [ 1, 2, 3 ]
        selection_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

    def test_selection_sort_unsorted(self):
        self.sut = [ 3, 1, 2 ]
        expected_list = [ 1, 2, 3 ]
        selection_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

    def test_selection_sort_duplicates(self):
        self.sut = [ 3, 1, 2, 2 ]
        expected_list = [ 1, 2, 2, 3 ]
        selection_sort(self.sut)
        self.assertEqual(self.sut, expected_list)
    #endregion
#endregion

if __name__ == "__main__":
    unittest.main(verbosity = 2)