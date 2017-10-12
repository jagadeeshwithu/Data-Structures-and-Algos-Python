"""
Merge two sorted LinkedLists
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} => {}".format(self.val, self.next)


class MergeSolution(object):
    def mergeLists(self, List1, List2):

        curr = dummy = ListNode(0)
        while List1 and List2:
            if List1.val < List2.val:
                curr.next = List1
                List1 = List1.next

            else:
                curr.next = List2
                List2 = List2.next

            curr = curr.next

        curr.next = List1 or List2
        return dummy.next


if __name__ == "__main__":

        l1 = ListNode(8)
        l2 = ListNode(55)
        l3 = ListNode(85)
        l31 = ListNode(87)

        l1.next = l2
        l2.next = l3
        l3.next = l31

        l4 = ListNode(43)
        l5 = ListNode(67)
        l6 = ListNode(94)

        l4.next = l5
        l5.next = l6

        print(l1)
        print(l4)
        print(MergeSolution().mergeLists(l1,l4))