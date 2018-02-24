# Completely silly exercises, in real life use:
# Python lists: https://docs.python.org/3/tutorial/datastructures.html

import unittest
import logging

logging.basicConfig(level = logging.INFO)

##- BinaryTree class.
# Search method not included, has its own category.
class BinaryTree:

    ##- Create. O(1).
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
    #-##

    ##- Delete. O(n) (sort of: garbage collection).
    def delete(self):
        self.top = None
    #-##  

    def insertLeft(self, element):
        if(self.leftNode == None):
            self.leftNode = BinaryTree(element)
        else:
            tempNode = BinaryTree(element)
            tempNode.leftNode = self.leftNode
            self.leftNode = tempNode

    def insertRight(self, element):
        if(self.rightNode == None):
            self.rightNode = BinaryTree(element)
        else:
            tempNode = BinaryTree(element)
            tempNode.rightNode = self.rightNode
            self.rightNode = tempNode

    def preorder_traverse(self, callback):
        if(self == None):
            return
        callback(self.value)
        self.leftNode.traverse()
        self.rightNode.traverse()

    def inorder_traverse(self, callback):
        if(self == None):
            return
        self.leftNode.traverse()
        callback(self.value)
        self.rightNode.traverse()

    def postorder_traverse(self, callback):
        if(self == None):
            return        
        self.leftNode.traverse()
        self.rightNode.traverse()
        callback(self.value)

    ##- Utility methods.
    def __str__(self):
        if(self == None):
            return ""
        stackString = str(self.value)
        logging.debug(self.value)
        if(self.leftNode != None):
            stackString += ", {}".format(self.leftNode.__str__())
        if(self.rightNode != None):
            stackString += ", {}".format(self.rightNode.__str__())
        return stackString
  
    def __eq__(self, other):
        if not self and not other:
            return True

        if(not isinstance(other, self.__class__)):
            return False        

        if self and other:
            if(self.value != other.value):            
                return False
            if self.leftNode:
                if not self.leftNode.__eq__(other.leftNode):
                    return False
            if self.rightNode:
                if not self.rightNode.__eq__(other.rightNode):
                    return False
            return True

        return False
    #-##
#-##

##- TestBinaryTree class.
class TestBinaryTree(unittest.TestCase):

    sut = None

    def setUp(self):
        self.sut = BinaryTree(1)

    def test_create(self):
        self.assertTrue(hasattr(self, "sut"))

    def test_delete(self):
        sut = BinaryTree(1)

        sut.delete()
        self.assertEqual(sut.top, None)

    def test_insert_left(self):
        self.sut.insertLeft(2)
        self.sut.insertLeft(3)

        expectedTree = BinaryTree(1)
        expectedTree.leftNode = BinaryTree(3)
        expectedTree.leftNode.leftNode = BinaryTree(2)
        
        self.assertEqual(self.sut, expectedTree)

#-##

if __name__ == "__main__":
    unittest.main(verbosity = 2)
