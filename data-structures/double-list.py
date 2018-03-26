# Completely silly exercises, in real life use:
# Python lists: https://docs.python.org/3/tutorial/datastructures.html

import unittest
import logging

logging.basicConfig(level=logging.INFO)


# - DoublyLinkedListNode class.
class DoublyLinkedListNode:
    value = None
    previousNode = None
    nextNode = None

    def __init__(self, value, previousNode, nextNode):
        self.value = value
        self.previousNode = previousNode
        self.nextNode = nextNode

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self.value == other.value
#-##

# - DoublyLinkedList class.
# Search method not included, has its own category.


class DoublyLinkedList:

    # - Create. O(1).
    def __init__(self):
        self.head = None
    #-##

    # - Delete. O(n) (sort of: garbage collection).
    def delete(self):
        self.head = None
    #-##

    # - Insert at start. O(1).
    def insert_start(self, element):
        tempNode = DoublyLinkedListNode(element, None, self.head)
        self.head = tempNode
    #-##

    # - Set at start. O(1).
    def set_start(self, element):
        self.head.value = element
    #-##

    # - Insert at arbitrary position. O(n).
    def insert_position(self, position, element):
        if(self.head is None):
            self.insert_start(element)
            return

        tempNode = DoublyLinkedListNode(element, None, None)

        current = self.head
        count = 0
        while((current.nextNode is not None) and (count < position)):
            count += 1
            current = current.nextNode

        tempNode.nextNode = current.nextNode
        tempNode.previousNode = current.previousNode
        current.nextNode.previousNode = tempNode
        current.nextNode = tempNode
    #-##

    # - Set at arbitrary position. O(n).
    def set_position(self, position, element):
        if(self.head is None):
            return

        current = self.head
        count = 0
        while((current.nextNode is not None) and (count < position)):
            count += 1
            current = current.nextNode
        current.value = element
    #-##

    # - Insert at end. O(n).
    def insert_end(self, element):
        if(self.head is None):
            self.insert_start(element)
            return

        tempNode = DoublyLinkedListNode(element, None, None)

        current = self.head
        count = 0
        while(current.nextNode is not None):
            count += 1
            current = current.nextNode

        tempNode.previousNode = current
        current.nextNode = tempNode
    #-##

    # - Set at end. O(n).
    def set_end(self, element):
        if(self.head is None):
            return

        current = self.head
        count = 0
        while(current.nextNode is None):
            count += 1
            current = current.nextNode

        current.value = element
    #-##

    # - Join. O(n).
    def join(self, other):
        if(self.head is None):
            self.insert_start(other)
            return

        current = self.head
        count = 0
        while(current.nextNode is not None):
            count += 1
            current = current.nextNode

        other.head.previousNode = current
        current.nextNode = other.head
    #-##

    # - Utility methods.
    def __str__(self):
        if(self.head is None):
            return ""

        listString = str(self.head)
        current = self.head.nextNode
        while(current is not None):
            listString += ", {}".format(str(current))
            current = current.nextNode

        return listString

    def __eq__(self, other):
        if(not isinstance(other, self.__class__)):
            return False

        currentSelf = self.head
        currentOther = other.head

        while(currentSelf is not None):
            if(currentOther is not None):
                # Different nodes.
                if(currentSelf.value != currentOther.value):
                    return False
                currentSelf = currentSelf.nextNode
                currentOther = currentOther.nextNode
            # We ran out of nodes in the other list.
            elif(currentOther is None):
                return False
        # We ran out of nodes in the self list.
        if(currentOther is not None):
            return False
        # Full comparison, everything the same.
        return True
    #-##
#-##

# - TestDoublyLinkedList class.


class TestDoublyLinkedList(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = DoublyLinkedList()
        # Since we're inserting from the start, the values are reversed.
        # So the actual list is [ 1, 2, 3 ].
        for i in range(3, 0, -1):
            self.sut.insert_start(i)

    def test_create(self):
        self.assertTrue(hasattr(self, "sut"))

    def test_delete(self):
        sut = DoublyLinkedList()
        sut.head = True
        sut.delete()
        self.assertEqual(sut.head, None)

    def test_insert_start(self):
        # Make an expected list of [ 0, 1, 2, 3 ].
        expectedList = DoublyLinkedList()
        for i in range(3, -1, -1):
            expectedList.insert_start(i)
        self.sut.insert_start(0)
        self.assertEqual(self.sut, expectedList)

    def test_set_start(self):
        # Make an expected list of [ 0, 2, 3 ].
        expectedList = DoublyLinkedList()
        for i in range(3, 1, -1):
            expectedList.insert_start(i)
        expectedList.insert_start(0)

        self.sut.set_start(0)
        self.assertEqual(self.sut, expectedList)

    def test_insert_position(self):
        expectedList = DoublyLinkedList()
        expectedList.insert_start(3)
        expectedList.insert_start(6)
        expectedList.insert_start(2)
        expectedList.insert_start(1)

        self.sut.insert_position(1, 6)
        self.assertEqual(self.sut, expectedList)

    def test_set_position(self):
        expectedList = DoublyLinkedList()
        expectedList.insert_start(6)
        expectedList.insert_start(2)
        expectedList.insert_start(1)

        self.sut.set_position(2, 6)

    def test_insert_end(self):
        expectedList = DoublyLinkedList()
        expectedList.insert_start(6)
        expectedList.insert_start(3)
        expectedList.insert_start(2)
        expectedList.insert_start(1)

        self.sut.insert_end(6)
        self.assertEqual(self.sut, expectedList)

    def test_set_end(self):
        expectedList = DoublyLinkedList()
        expectedList.insert_start(6)
        expectedList.insert_start(2)
        expectedList.insert_start(1)

        self.sut.set_end(6)
        self.assertEqual(self.sut, expectedList)

    def test_join(self):
        expectedList = DoublyLinkedList()
        expectedList.insert_start(5)
        expectedList.insert_start(4)
        expectedList.insert_start(3)
        expectedList.insert_start(2)
        expectedList.insert_start(1)

        otherList = DoublyLinkedList()
        otherList.insert_start(5)
        otherList.insert_start(4)

        self.sut.join(otherList)
        self.assertEqual(self.sut, expectedList)
        self.assertEqual(self.sut, expectedList)
#-##


if __name__ == "__main__":
    unittest.main(verbosity=2)
