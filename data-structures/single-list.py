import unittest
import logging

logging.basicConfig(level = logging.INFO)

##- SinglyLinkedListNode class.
class SinglyLinkedListNode:
    value = None
    nextNode = None

    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self.value == other.value
#-##

##- SinglyLinkedList class.
# Search method not be included, has its own category.
class SinglyLinkedList:

    ##- Create. O(1).
    def __init__(self):
        self.head = None
    #-##

    ##- Delete. O(1) (sort of: garbage collection).
    def delete(self):
        self.head = None
    #-##

    ##- Insert at start. O(1).
    def insert_start(self, element):
        tempNode = SinglyLinkedListNode(element, self.head)
        self.head = tempNode
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

##- TestSinglyLinkedList class.
class TestSinglyLinkedList(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = SinglyLinkedList()
        for i in range(3, 0, -1):
            tempNode = SinglyLinkedListNode(i, self.sut.head)
            self.sut.head = tempNode

    def test_create(self):
        self.assertTrue(hasattr(self, "sut"))

    def test_delete(self):
        sut = SinglyLinkedList()
        sut.head = True
        sut.delete()
        self.assertEqual(sut.head, None)

    def test_insert_start(self):
        expectedList = SinglyLinkedList()
        for i in range(3, -1, -1):
            tempNode = SinglyLinkedListNode(i, expectedList.head)
            expectedList.head = tempNode
        self.sut.insert_start(0)
        self.assertEqual(self.sut, expectedList)
#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)
