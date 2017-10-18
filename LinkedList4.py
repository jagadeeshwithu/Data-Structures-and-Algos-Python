"""
Find intersection of two Linked Lists

Time: O(m + n)
Space: O(1)

For Example,

A:           5 - 6
                     \
                        7 - 8 - 9
                     /
B:     1 - 2 - 3 - 4


If there is no intersection return 'Null'

Assumptions:

1. No 'loops' in the given linked lists
2. assuming they are of different lengths
"""


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self:
            return " {} -> {} ".format(self.data, self.next)


class Intersection(object):
    def getIntersectionNode(self, list1, list2):

        temp1, temp2, currNode = list1, list2, 0

        len1, len2, diff = 0, 0, 0

        while temp1:
            len1 += 1
            temp1 = temp1.next

        while temp2:
            len2 += 1
            temp2 = temp2.next


        if len1 > len2:
            diff = len1 - len2
            currNode = list1
            temp = list2

        else:
            diff = len2 - len1
            currNode = list2
            temp = list1

        while diff:
            currNode = currNode.next
            diff -= 1

        while currNode != temp:
            currNode = currNode.next
            temp = temp.next

        return currNode


if __name__ == "__main__":

        l1 = ListNode(5)
        l2 = ListNode(6)
        l31 = ListNode(25)
        l3 = ListNode(7)
        l4 = ListNode(8)
        l5 = ListNode(9)
        l6 = ListNode(10)

        l1.next = l2
        l2.next = l31
        l31.next = l3
        l3.next = l4
        l4.next = l5
        l5.next = l6

        List1 = l1
        print(List1)

        l7 = ListNode(1)
        l8 = ListNode(2)
        l9 = ListNode(3)
        l10 = ListNode(4)
        l11 = ListNode(13)
        l12 = ListNode(26)

        l7.next = l8
        l8.next = l9
        l9.next = l10
        l10.next = l11
        l11.next = l12
        l12.next = l3
        l3.next = l4
        l4.next = l5
        l5.next = l6

        List2 = l7

        print(List2)

        intersect = Intersection()
        print(intersect.getIntersectionNode(List2,List1))