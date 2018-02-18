import unittest
import logging

logging.basicConfig(level = logging.INFO)

##- Array class.
# Will only simulate C-like array behavior.
# Some of these operations don't really make sense on Python "arrays" are actually
# a more complex data structure based on lists. Still, will go through the steps
# just as "practice".
# Search method not included, has its own category.
class Array:
    value = None

    ##- Create. O(1).
    def __init__(self, value = []):
        self.value = value
    #-##

    ##- Delete. O(1).
    def delete(self):
        self.value = None
    #-##

    ##- Insert at the start. O(1).
    # Doesn't really make sense for Python array. For normal, fixed-sized arrays
    # every insert requires creating a new array and copying the existing contents
    # "around" the insert.
    def insert_start(self, element):
        self.value = [ element ] + self.value
    #-##

    ##- Set at the start. O(1).
    def set_start(self, element):
        self.value[0] = element
    #-##

    ##- Insert at arbitrary position. O(1).
    def insert_position(self, position, element):
        arrayLength = len(self.value)
        self.value = self.value[:position + 1] + [ element ] \
            + self.value[position + 1:]
    #-##

    ##- Set at arbitrary position. O(1).
    def set_position(self, position, element):
        self.value[position] = element
    #-##

    ##- Insert at the end. O(1).
    def insert_end(self, element):
        self.value += [ element ]
    #-##

    ##- Set at the end.
    def set_end(self, element):
        self.value[len(self.value) - 1] = 5
    #-##

    ##- Join with fixed-sized arrays imply creating a new array with size M + N.
    # With Python we "cheat".
    def join(self, otherArray):
        self += otherArray
    #-##

    ##- Utility methods.
    def __str__(self):
        return str(self.value)

    def __len__(self):
        return len(self.value)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.value == other.value

    def __iadd__(self, other):
        self.value += other.value
        return self
    #-##
#-##

##- TestArray class.
class TestArray(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = Array([ 1, 2, 3 ])

    def test_create(self):
        self.assertTrue(hasattr(self, "sut"))

    def test_delete(self):
        sut = Array([1, 2, 3])
        sut.delete()
        self.assertFalse(sut.value, None)

    def test_insert_start(self):
        self.sut.insert_start(0)
        self.assertEqual(self.sut, Array([ 0, 1, 2, 3 ]))

    def test_set_start(self):
        self.sut.set_start(0)
        self.assertEqual(self.sut, Array([ 0, 2, 3 ]))

    def test_insert_position(self):
        self.sut.insert_position(len(self.sut) // 2, 5)
        self.assertEqual(self.sut, Array([ 1, 2, 5, 3 ]))

    def test_set_position(self):
        self.sut.set_position(len(self.sut) // 2, 5)
        self.assertEqual(self.sut, Array([ 1, 5, 3 ]))

    def test_insert_end(self):
        self.sut.insert_end(5)
        self.assertEqual(self.sut, Array([ 1, 2, 3, 5 ]))

    def test_set_end(self):
        self.sut.set_end(5)
        self.assertEqual(self.sut, Array([ 1, 2, 5 ]))

    def test_join(self):
        self.sut.join(Array([ 6, 7 ]))
        self.assertEqual(self.sut, Array([ 1, 2, 3, 6, 7 ]))
#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)
