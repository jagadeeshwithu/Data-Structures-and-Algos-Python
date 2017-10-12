"""
Reverse LinkedList: Recursive
"""

from LinkedList import LList


class LinkedList(LList):
    def reverseRecurse(self, currNode):
        if currNode == None:
            return
        if currNode.getNext() == None:
            self.head = currNode
            return
        self.reverseRecurse(currNode.getNext())
        currNode.getNext().setNext(currNode)
        currNode.setNext(None)


if __name__ == '__main__':
        myList = LinkedList()
        myList.add(5)
        myList.add(8)
        myList.add(12)
        myList.add(34)
        myList.add(43)
        myList.add(82)

        print (myList.printlist())
        #print (myList.head.getNext().getNext().data)
        myList.reverseRecurse(myList.head)
        print (myList.printlist())
