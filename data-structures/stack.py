import unittest
import logging

logging.basicConfig(level = logging.INFO)

##- StackNode class.
class StackNode:
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

##- Stack class.
# Search method not included, has its own category.
class Stack:

    ##- Create. O(1).
    def __init__(self):
        self.top = None
    #-##

    ##- Delete. O(n) (sort of: garbage collection).
    def delete(self):
        self.top = None
    #-##

    ##- Push. O(1).
    def push(self, element):
        tempNode = StackNode(element, self.top)
        self.top = tempNode
    #-##

    ##- Pop. O(1).
    def pop(self):
        if(self.top == None):
            return

        value = self.top.value

        if(self.top.nextNode == None):
            self.top = None
        else:
            self.top = self.top.nextNode

        return value
    #-##

    ##- Peek. O(1).
    def peek(self):
        if(self.top == None):
            return

        return self.top.value
    #-##

    ##- Size. O(n).
    def size(self):
        size = 0
        if(self.top == None):
            return size

        size = 1
        current = self.top.nextNode
        while(current != None):
            current = current.nextNode
            size += 1

        return size
    #-##

    ##- Utility methods.
    def __str__(self):
        if(self.top == None):
            return ""

        stackString = str(self.top)
        current = self.top.nextNode
        while(current != None):
            stackString += ", {}".format(str(current))
            current = current.nextNode

        return stackString

    def __eq__(self, other):
        if(not isinstance(other, self.__class__)):
            return False

        currentSelf = self.top
        currentOther = other.top

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

##- TestStack class.
class TestStack(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = Stack()
        # Since we're inserting from the start, the values are reversed.
        # So the actual list is [ 1, 2, 3 ].
        for i in range(3, 0, -1):
            self.sut.push(i)

    def test_create(self):
        self.assertTrue(hasattr(self, "sut"))

    def test_delete(self):
        sut = Stack()
        sut.top = True

        sut.delete()
        self.assertEqual(sut.top, None)

    def test_push(self):
        # Make an expected stack of [ 0, 1, 2, 3 ].
        expectedStack = Stack()
        for i in range(3, -1, -1):
            expectedStack.push(i)

        self.sut.push(0)
        self.assertEqual(self.sut, expectedStack)

    def test_pop(self):
        # Make an expected stack of [ 2, 3 ].
        expectedStack = Stack()
        expectedStack.push(3)
        expectedStack.push(2)

        value = self.sut.pop()

        self.assertEqual(value, 1)
        self.assertEqual(self.sut, expectedStack)

    def test_peek(self):
        value = self.sut.peek()

        self.assertEqual(value, 1)

    def test_size(self):
        size = self.sut.size()

        self.assertEqual(size, 3)
#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)
