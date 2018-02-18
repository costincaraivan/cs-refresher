# Completely silly exercises, in real life use:
# Python lists: https://docs.python.org/3/tutorial/datastructures.html

import unittest
import logging

logging.basicConfig(level = logging.INFO)

##- QueueNode class.
class QueueNode:
    value = None
    previousNode = None

    def __init__(self, value, previousNode):
        self.value = value
        self.previousNode = previousNode

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self.value == other.value
#-##

##- Queue class.
# Search method not included, has its own category.
class Queue:

    ##- Create. O(1).
    def __init__(self):
        self.tail = None
        self.head = None
    #-##

    ##- Delete. O(n) (sort of: garbage collection).
    def delete(self):
        self.tail = None
        self.head = None
    #-##

    ##- Enqueue. O(1).
    def enqueue(self, element):
        if(self.head == None):
            tempNode = QueueNode(element, None)
            self.head = tempNode
            self.tail = tempNode
        else:
            tempNode = QueueNode(element, None)
            self.tail.previousNode = tempNode
            self.tail = tempNode
    #-##

    ##- Dequeue. O(1).
    def dequeue(self):
        if(self.head == None):
            return

        value = self.head.value
        self.head = self.head.previousNode

        return value
    #-##

    ##- Size. O(n).
    def size(self):
        size = 0
        if(self.head == None):
            return size

        size = 1
        current = self.head.previousNode
        while(current != None):
            current = current.previousNode
            size += 1

        return size
    #-##

    ##- Utility methods.
    def __str__(self):
        if(self.head == None):
            return ""

        stackString = str(self.head)
        current = self.head.previousNode
        while(current != None):
            stackString += ", {}".format(str(current))
            current = current.previousNode

        return stackString

    def __eq__(self, other):
        if(not isinstance(other, self.__class__)):
            return False

        currentSelf = self.head
        currentOther = other.head

        while(currentSelf != None):
            if(currentOther != None):
                # Different nodes.
                if(currentSelf.value != currentOther.value):
                    return False
                currentSelf = currentSelf.previousNode
                currentOther = currentOther.previousNode
            # We ran out of nodes in the other list.
            elif(currentOther == None):
                return False
        # We ran out of nodes in the self list.
        if(currentOther != None):
            return False
        # Full comparison, everything the same.
        return True
    #-##
#-##

##- TestQueue class.
class TestQueue(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = Queue()
        # Since we're inserting from the start, the values are reversed.
        # So the actual list is [ 1, 2, 3 ].
        for i in range(1, 4, 1):
            self.sut.enqueue(i)

    def test_create(self):
        self.assertTrue(hasattr(self, "sut"))

    def test_delete(self):
        sut = Queue()
        sut.head = True

        sut.delete()
        self.assertEqual(sut.head, None)

    def test_enqueue(self):
        # Make an expected stack of [ 0, 1, 2, 3 ].
        expectedQueue = Queue()
        for i in range(1, 5, 1):
            expectedQueue.enqueue(i)

        self.sut.enqueue(4)
        self.assertEqual(self.sut, expectedQueue)

    def test_dequeue(self):
        # Make an expected stack of [ 2, 3 ].
        expectedQueue = Queue()
        expectedQueue.enqueue(2)
        expectedQueue.enqueue(3)

        value = self.sut.dequeue()

        self.assertEqual(value, 1)
        self.assertEqual(self.sut, expectedQueue)

    def test_size(self):
        size = self.sut.size()
        self.assertEqual(size, 3)
#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)
