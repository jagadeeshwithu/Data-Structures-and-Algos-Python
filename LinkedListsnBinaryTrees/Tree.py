"""
Implementation of Tree and operations include,

1. Tree Insertion: Insert Right child, and Insert left child
2. Tree traversals: Pre Order, In Order and Post Order

Note:
"""


class BinaryTree(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def insertRight(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.right = self.right
            self.right = tree

    def insertLeft(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            self.left = tree
            tree.left = self.left


def printTree(tree):
    if tree is not None:
        printTree(tree.left)
        print(tree.data)
        printTree(tree.right)


if __name__ == "__main__":

        myTree = BinaryTree("a")
        myTree.insertLeft("b")
        myTree.insertRight("c")
        myTree.insertRight("d")
        printTree(myTree)