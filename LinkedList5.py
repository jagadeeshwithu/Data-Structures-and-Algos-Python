"""
To Detect a loop in a linked list

Also called Floyd's loop detection algorithm

We also implement removal of loop in this module
"""


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self:
            return "{} => {}".format(self.data, self.next)


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def detectAndRemoveLoop(self):
        slow = fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.removeLoop(slow)

                return True

        return False

    def removeLoop(self, loop):

        temp = self.head

        while True:
            loopNode = loop
            while loopNode.next != loop and loopNode.next != temp:
                loopNode = loopNode.next

            if loopNode.next == temp:
                break

            temp = temp.next


        loopNode.next = None

    def add(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    def printlist(self):
        temp = self.head
        print(temp)


if __name__ == "__main__":

        llist = LinkedList()
        llist.add(10)
        llist.add(4)
        llist.add(15)
        llist.add(20)
        llist.add(50)
        llist.add(34)

        llist.printlist()

        llist.head.next.next.next.next = llist.head.next.next

        llist.detectAndRemoveLoop()

        print("Linked List after removal of Loop")
        llist.printlist()

