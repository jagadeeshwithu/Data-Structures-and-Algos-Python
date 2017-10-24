"""
Implement basic Binary Search Tree

Traversals: 1. Inorder, 2. Preorder and 3. Postorder

Assumptions: No duplicates allowed
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        elif self.data < data:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Node(data)

    def preorder(self):
        if self:
            print(self.data)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.data)
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data)


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def preorder(self):
        if self.root is not None:
            print("Preorder:")
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            print("Inorder:")
            self.root.inorder()

    def postorder(self):
        if self.root is not None:
            print("Postorder:")
            self.root.postorder()


if __name__ == "__main__":

        bst = BST()
        bst.insert(10)
        bst.insert(25)
        bst.insert(8)
        bst.insert(13)
        bst.insert(55)
        bst.insert(4)
        bst.insert(6)
        bst.insert(12)
        bst.insert(9)

        bst.inorder()
        #bst.remove(9)

        bst.postorder()
        bst.preorder()
