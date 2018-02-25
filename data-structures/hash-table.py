# Completely silly exercises, in real life use:
# Python lists: https://docs.python.org/3/tutorial/datastructures.html

import unittest
import logging

logging.basicConfig(level = logging.INFO)

##- HashTableEntry class.
class HashTableEntry:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("{}: {}".format(self.key, self.value))

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self.key == other.key \
            and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)
#-##

##- HashTable class.
class HashTable:

    TABLE_SIZE = 1123

    table = None

    ##- Create. O(1).
    def __init__(self):
        # Arbitrary hash table size: 1123 (prime number, to distributes things evenly into buckets).
        # The actual size is for demo purposes, normally it is selected based on the problem domain.
        # I.e. > 20 million for the population of Romania, etc.
        self.table = [ [] for index in range(self.TABLE_SIZE) ]
    #-##

    ##- Delete. O(1) (sort of: garbage collection).
    def delete(self):
        self.table = None
    #-##

    ##- Hash. Used to determine the bucket where to put the element.
    def hash(self, entry):
        if entry == None:
            raise KeyError("Trying to hash None entry.")
        if entry.key == None:
            raise KeyError("Trying to hash None key.")
        hash_value = 7
        for letter in entry.key:
            # 31 is the selected prime number in Java string hashing implementation.
            # Which, hopefully, has a decent hashing algorithm :)
            hash_value = self.__multiply_32bit(31, hash_value)
            hash_value = self.__add_32bit(hash_value, ord(letter))
        return hash_value % self.TABLE_SIZE
    #-##

    ##- 32 bit integer operations.
    # Restricting the size of the infinite-precision Python integers to 32 bits
    # by masking the numbers to 32 bits (binary and with 1s).
    __bit_mask = 0xFFFFFFFFL

    def __mask_32bit(self, my_number):
        return my_number & self.__bit_mask
    def __add_32bit(self, my_number, other_number):
        return self.__mask_32bit(my_number + other_number)
    def __multiply_32bit(self, my_number, other_number):
        return self.__mask_32bit(my_number * other_number)
    #-##

    ##- Put. O(1).
    def put(self, my_entry):
        hash_value = self.hash(my_entry)      
        # There's no collision, just add the value.
        if(self.table[hash_value] == []):
            self.table[hash_value].append(my_entry)
            return
        # There's a collision and the element was found, just update its value.
        for entry in self.table[hash_value]:
            if my_entry.key == entry.key:
                entry.value = my_entry.value
                return
        # There's a collision and the element was not found, add it at the end of the list.
        self.table[hash_value][len(self.table[hash_value]) - 1].append(my_entry)
    #-##

    ##- Get. O(1).
    def get(self, my_key):
        hash_value = self.hash(HashTableEntry(my_key, ""))
        if(self.table[hash_value] == None):
            return None
        if(len(self.table[hash_value]) == 1):
            return self.table[hash_value][0].value
        for entry in self.table[hash_value]:
            if my_key == entry.key:
                return entry.value
    #-##

    ##- Utility methods.
    def __str__(self):
        hashTableString = ""
        for index in range(len(self.table)):
            if self.table[index] == []:
                pass          
            for entry in self.table[index]:                
                hashTableString += "{}: {}".format(index, str(entry))
        return hashTableString

    def __eq__(self, other):
        # Both None.
        if self is None and other is None:
            return True
        # Different lengths.
        if len(self.table) != len(other.table):
            return False
        # Go through each bucket.
        for bucket_index in range(len(self.table)):
            # Different bucket lengths.
            if len(self.table[bucket_index]) != len(other.table[bucket_index]):
                return False
            # Skip empty buckets.
            if self.table[bucket_index] == [] and other.table[bucket_index] == []:
                pass
            for collision_index, entry in enumerate(self.table[bucket_index]):
                if entry != other.table[bucket_index][collision_index]:
                    return False
        return True           
    #-##
#-##

##- TestHashTable class.
class TestHashTable(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = HashTable()

    def test_create(self):
        self.assertTrue(hasattr(self, "sut"))

    def test_delete(self):
        sut = HashTable()
        sut.table = True

        sut.delete()
        self.assertEqual(sut.table, None)

    def test_hash_none_entry(self):
        with self.assertRaises(KeyError) as raises:
            self.sut.hash(None)
        self.assertEqual(raises.exception.message, "Trying to hash None entry.")

    def test_hash_none_key(self):
        with self.assertRaises(KeyError) as raises:
            self.sut.hash(HashTableEntry(None, "value"))
        self.assertEqual(raises.exception.message, "Trying to hash None key.")

    def test_put(self):
        expectedHashTable = HashTable()
        expectedHashTable.table[797].append(HashTableEntry("hello world!", "ole"))

        self.sut.put(HashTableEntry("hello world!", "ole"))
        self.assertEqual(self.sut, expectedHashTable)

    def test_get(self):
        self.sut.table[797].append(HashTableEntry("hello world!", "ole"))

        self.assertEqual(self.sut.get("hello world!"), "ole")
#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)
