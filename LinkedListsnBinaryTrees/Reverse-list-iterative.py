"""
Implement reverse Linked List - Iterative way
"""

from LinkedList import LinkedList


class LinkedList1(LinkedList):
    def reverse_list(self):
        fp, sp, lp = None, None, self.head

        while lp is not None:

            sp = lp
            lp = lp.next_node
            sp.next_node = fp
            fp = sp

        return sp


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
