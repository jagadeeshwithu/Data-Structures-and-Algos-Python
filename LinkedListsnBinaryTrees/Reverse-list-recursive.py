"""
Reverse Linked List - Recursive way
"""


from LinkedList import LinkedList


class LinkedList1(LinkedList):
    def reverse_list(self):
        headptr = self.head
        return self._reverse(headptr)

    def _reverse(self, head, prev=None):
        if head is None:
            return prev
        n = head.next_node
        head.next_node = prev
        return self._reverse(n, head)


if __name__ == "__main__":

    list1 = LinkedList1()
    list1.add_beginning(13)
    list1.add_beginning(26)
    list1.add_beginning(18)
    list1.add_beginning(52)
    list1.add_beginning(43)
    list1.add_ending(25)
    list1.add_ending(55)

    print(list1)

    print(list1.reverse_list())


