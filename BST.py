"""
Binary Search Tree implementation

Assumption:

1. Duplicate values not allowed, logic implemented in 'if' statement with insert function
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        elif self.value < data:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print("Pre order")
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("Post order")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("In order")
            self.root.inorder()


if __name__ == "__main__":


    bst = Tree()
    print(bst.insert(10))
    print(bst.insert(25))
    print(bst.insert(8))
    print(bst.insert(13))
    print(bst.insert(55))
    print(bst.insert(4))
    print(bst.insert(6))
    print(bst.insert(12))
    print(bst.insert(9))

    bst.postorder()
    bst.preorder()
    bst.inorder()