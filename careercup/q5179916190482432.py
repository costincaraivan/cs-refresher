# https://careercup.com/question?id=5179916190482432
# input [2,3,1,4], output [12,8,24,6]
# Multiply all fields except its own position.
# Restrictions: 1. no use of division, 2. complexity in O(n)

import unittest
import logging

logging.basicConfig(level = logging.INFO)


def multiply_array(input_array):
    front = [ 1 ] * len(input_array)
    rear = [ 1 ] * len(input_array)
    output_array = [ 1 ] * len(input_array)

    for i in range(1, len(input_array)):
        front[i] = front[i - 1] * input_array[i - 1]

    for j in range(len(input_array) - 2, -1, -1):
        rear[j] = rear[j + 1] * input_array[j + 1]

    for k in range(len(input_array)):
        output_array[k] = front[k] * rear[k]

    return output_array


class TestMultiplyArray(unittest.TestCase):
    def test_multiply_array(self):
        input_array = [ 2, 3, 1, 4 ]
        output_array = multiply_array(input_array)

        self.assertEqual(output_array, [12, 8, 24, 6])

if __name__ == "__main__":
    unittest.main(verbosity = 2)