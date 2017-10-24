"""
Detect a loop in the given list and return the node
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "{} -> {}".format(self.data, self.next_node)


class LinkedList:
    def loop_detection(self, A):

        slow = fast = A

        while fast is not None:
            slow = slow.next_node

            if fast.next_node is not None:
                fast = fast.next_node.next_node
            else:
                return False

            if slow is fast:
                return slow

        return False


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
        l8.next_node = l5

        #print(l1)
        print ("The Node where loop has been detected:", end=" ")
        print(LinkedList().loop_detection(l1).data)