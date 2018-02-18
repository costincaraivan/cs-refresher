import unittest
import logging

logging.basicConfig(level = logging.INFO)

##- DoublyLinkedListNode class.
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

##- DoublyLinkedList class.
# Search method not included, has its own category.
class DoublyLinkedList:

    ##- Create. O(1).
    def __init__(self):
        self.head = None
    #-##

    ##- Delete. O(n) (sort of: garbage collection).
    def delete(self):
        self.head = None
    #-##

    ##- Insert at start. O(1).
    def insert_start(self, element):
        tempNode = DoublyLinkedListNode(element, None, self.head)
        self.head = tempNode
    #-##

    ##- Set at start. O(1).
    def set_start(self, element):
        self.head.value = element
    #-##

    ##- Utility methods.
    def __str__(self):
        if(self.head == None):
            return ""

        listString = str(self.head)
        current = self.head.nextNode
        while(current != None):
            listString += ", {}".format(str(current))
            current = current.nextNode

        return listString

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
                currentSelf = currentSelf.nextNode
                currentOther = currentOther.nextNode
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


##- TestDoublyLinkedList class.
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
#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)
