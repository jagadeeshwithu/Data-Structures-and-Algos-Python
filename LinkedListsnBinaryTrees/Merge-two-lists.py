"""
Implement merge function for two sorted lists

Assumptions: Sorted lists are passed as inputs
"""


from LinkedList import LinkedList, Node


class LinkedList1(LinkedList):
    def merge_two_lists(self, A, B):
        """
            This implementation would take two lists as arguments and does 'Merge' function
        """
        mergedlist = dummy = Node(0)
        one, two = A.head, B.head
        while one and two:
            if one.data < two.data:
                mergedlist.next_node = one
                one = one.next_node
            else:
                mergedlist.next_node = two
                two = two.next_node

            mergedlist = mergedlist.next_node

        mergedlist.next_node = one or two

        return dummy.next_node

    def merge_two_lists1(self, A):
        """
        Takes the other (sorted) list to be merged with!
        :param A: list2 passed as argument to be merged with list1 as calling
        :return: returns the merged list
        """
        mergedlist = dummy = Node(0)
        first, second = self.head, A.head

        while first and second:
            if first.data < second.data:
                mergedlist.next_node = first
                first = first.next_node
            else:
                mergedlist.next_node = second
                second = second.next_node

            mergedlist = mergedlist.next_node

        mergedlist.next_node = first or second

        return dummy.next_node


if __name__ == "__main__":

        list1 = LinkedList1()
        list1.add_beginning(9)
        list1.add_beginning(7)
        list1.add_beginning(5)
        list1.add_beginning(3)
        list1.add_beginning(1)

        print(list1)

        list2 = LinkedList1()
        #list2.add_ending(0) : This case need to be handled
        list2.add_beginning(6)
        list2.add_beginning(4)
        list2.add_beginning(2)
        list2.add_ending(8)

        print(list2)

        #print(list2.merge_two_lists(list1, list2))
        print(list2.merge_two_lists1(list1))

