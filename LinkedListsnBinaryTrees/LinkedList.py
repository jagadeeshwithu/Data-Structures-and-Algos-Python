"""
Implementing Basic Linked List

Assumptions: Empty header, pointing to the linked list, used for all operations, include

                1. Insert at Beginning,
                2. Insert at End
                3. Deletion at Beginning,
                4. Deletion at the end
                5. get the size of the linked list
                6. Find the element
                7. print the list (used in-built __repr__ function to optimize and style the printing)
"""


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.data, self.next_node)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        curr = self.head
        if curr is not None:
            return str(curr)

    def add_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def add_ending(self, data):
        curr = self.head
        while curr.next_node is not None:
            curr = curr.next_node
        new_node = Node(data, curr.next_node)
        curr.next_node = new_node

    def remove_beginning(self):
        curr = self.head
        self.head = curr.next_node

    def remove_ending(self):
        curr = self.head
        while True:
            if curr.next_node.next_node is None:
                curr.next_node = None
                return curr
            curr = curr.next_node

    def get_size(self):
        curr = self.head
        size = 0
        while curr is not None:
            size += 1
            curr = curr.next_node

        return size

    def find(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return True
            curr = curr.next_node

        return False


if __name__ == "__main__":

        list1 = LinkedList()

        list1.add_beginning(3)
        list1.add_beginning(6)
        list1.add_ending(1)
        list1.add_ending(2)
        list1.add_ending(4)
        list1.add_beginning(9)
        list1.add_beginning(12)
        list1.add_beginning(25)

        print(list1)
        print(list1.get_size())

        list1.remove_beginning()
        list1.remove_ending()

        print(list1)
        print(list1.get_size())

        print(list1.find(2))