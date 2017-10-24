"""
Implementation for locating the intersection of two linked lists:

Solving the O(m+n) Time Complexity
"""


from LinkedList import LinkedList, Node


class LinkedList1(LinkedList):
    def find_intersection(self, A, B):
        """

        :param A: Passed the list to be check the intersection
        :return: the list where intersection begins
        """
        first, second = A, B

        size1, size2 = 0, 0

        while first:
            size1 += 1
            first = first.next_node

        while second:
            size2 += 1
            second = second.next_node

        if size1 < size2:
            diff = size2 - size1
            temp = A
            curr = B

        else:
            diff = size1 - size2
            temp = B
            curr = A

        while diff != 0:
            curr = curr.next_node
            diff -= 1

        while curr != temp:
            curr = curr.next_node
            temp = temp.next_node

        return curr


if __name__ == "__main__":

        l1 = Node(1)
        l2 = Node(2)
        l3 = Node(3)
        l4 = Node(4)
        l5 = Node(5)
        l6 = Node(6)
        l7 = Node(7)
        l8 = Node(8)

        l1.next_node = l2
        l2.next_node = l3
        l3.next_node = l4
        l4.next_node = l5
        l5.next_node = l6
        l6.next_node = l7
        l7.next_node = l8

        print(l1)

        l9 = Node(9)
        l10 = Node(10)

        l9.next_node = l10
        l10.next_node =l7

        print(l9)

        print("The intersection point would be:")
        print(LinkedList1().find_intersection(l1, l9))
