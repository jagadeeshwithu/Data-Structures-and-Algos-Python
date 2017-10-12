"""
Reverse LinkedList: Iterative way
"""

from LinkedList import LList


class LinkedList(LList):
    def reverseIterative(self):
        prevNode = None
        currNode = self.head
        nextNode = None
        while currNode is not None:
            nextNode = currNode.getNext()
            currNode.setNext(prevNode)
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode


if __name__ == '__main__':

        myList = LinkedList()
        myList.add(5)
        myList.add(8)
        myList.add(12)
        myList.add(34)
        myList.add(43)
        myList.add(82)

        print (myList.printlist())
        myList.reverseIterative()
        print (myList.printlist())
