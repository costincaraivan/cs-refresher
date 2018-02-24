# Completely silly exercises, in real life use:
# Python lists: https://docs.python.org/3/tutorial/datastructures.html

import unittest
import logging

logging.basicConfig(level = logging.INFO)

def bubble_sort(my_list):
    for number_passes in range(len(my_list) - 1, 0, -1):
        for index in range(number_passes):
            if my_list[index] > my_list[index + 1]:
                my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

##- TestBubbleSort class.
class TestBubbleSort(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = []

    def test_sort_empty(self):
        expected_list = []
        bubble_sort(self.sut)        
       
        self.assertEqual(self.sut, expected_list)

    def test_sort_sorted(self):
        self.sut = [ 1, 2, 3 ]
        expected_list = [ 1, 2, 3 ]
        bubble_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

    def test_sort_unsorted(self):
        self.sut = [ 3, 1, 2 ]
        expected_list = [ 1, 2, 3 ]
        bubble_sort(self.sut)
        self.assertEqual(self.sut, expected_list)

#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)