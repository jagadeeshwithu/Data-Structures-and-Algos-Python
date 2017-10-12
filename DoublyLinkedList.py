"""
Implementing Doubly Linked Lists

operations implemented:

1. Insert at the front: addFirst()
2. Insert at the last: addLast()
3. Remove from the front: popFirst()
4. Remove from the last: popLast()
5. __repr__ function for printing the list
6. 'Node' child class for individual node with data, and pointers to previous(prevNode) and next(nextNode)

"""


class DoublyLinkedList(object):
    class Node(object):
        def __init__(self, data, prevNode, nextNode):
            self.data = data
            self.prevNode = prevNode
            self.nextNode = nextNode

    def __init__(self, data = None):
        self.first = None
        self.last = None
        self.count = 0

    def addFirst(self, data):
        if self.first is None:
            self.first = self.Node(data, None, None)
            self.last = self.first
        else:
            node = self.Node(data, None, self.first)
            self.first.prevNode = node
            self.first = node

        self.current = self.first
        self.count += 1


    def popFirst(self):
        if self.first is None:
            raise RuntimeError("Cannot pop from an empty linked list")
        result = self.first.data
        if self.count == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.nextNode
            self.first.prevNode = None
        self.current = self.first
        self.count -= 1
        return result

    def popLast(self):
        if self.first is None:
            raise RuntimeError("cannot pop from an empty linked list")
        result = self.last.data
        if self.count == 1:
            self.first = None
            self.last = None
        else:
            self.last = self.last.prevNode
            self.last.nextNode = None
        self.count -= 1
        return result

    def addLast(self, data):
        if self.first is None:
            self.addFirst(0)
        else:
            self.last.nextNode = self.Node(data, self.last, None)
            self.last = self.last.nextNode
            self.count += 1

    def __repr__(self):
        result = ""
        if self.first is None:
            return "..."
        cursor = self.first
        for i in range(self.count):
            result += "{}".format(cursor.data)
            cursor = cursor.nextNode
            if cursor is not None:
                result += " <=> "
        return result

    def __iter__(self):
        return self

    def next(self):
        if self.current is None:
            self.current = self.first
            raise StopIteration
        else:
            result = self.current.data
            self.current = self.current.nextNode
            return result

    def __len__(self):
        return self.count



if __name__ == "__main__":

        dll = DoublyLinkedList()
        dll.addFirst(1)
        dll.addFirst(2)
        dll.addLast(3)
        dll.addFirst(4)
        dll.addFirst(5)
        dll.addLast(6)
        dll.addFirst(7)
        dll.addFirst(8)
        dll.addLast(9)

        print(dll)

        print(len(dll))

        dll.popFirst()
        dll.popLast()

        print(dll)

        print(len(dll))

        dll.addLast(10)
        dll.addFirst(11)

        print(dll)

        print(len(dll))
