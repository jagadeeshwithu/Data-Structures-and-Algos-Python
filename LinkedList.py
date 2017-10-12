"""
Basic Linked Lists implementation with Node and LinkedList classes defined

Assumptions:
------------

1. Node will be added at the head every time

"""

class Node(object):
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.nextNode

    def setNext(self, nextNode):
        self.nextNode = nextNode


class LList(object):
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def getSize(self):
        return self.size

    def add(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
        self.size += 1

    def remove(self, data):
        currNode = self.head
        prevNode = None
        while currNode:
            if currNode.getData() == data:
                if prevNode:
                    prevNode.setNext(currNode.getNext())
                else:
                    self.head = currNode.getNext()
                self.size -= 1
                return True
            else:
                prevNode = currNode
                currNode = currNode.getNext()
        return False

    def find(self, data):
        currNode = self.head
        while currNode:
            if currNode.getData() == data:
                return True
            else:
                currNode = currNode.getNext()
        return False

    def printlist(self):
        currNode = self.head
        while currNode != None:
            print(currNode.data, end=' => ')
            currNode = currNode.getNext()


if __name__ == '__main__':

        myList = LList()
        myList.add(5)
        myList.add(8)
        myList.add(12)
        myList.add(34)
        myList.add(43)
        myList.add(82)

        print (myList.printlist())
        myList.remove(12)
        myList.remove(82)
        print (myList.printlist())
        print(myList.find(34))
        print (myList.printlist())
