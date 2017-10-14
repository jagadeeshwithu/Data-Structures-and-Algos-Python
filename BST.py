"""
Binary Search Tree implementation

Assumption:

1. Duplicate values not allowed, logic implemented in 'if' statement with insert function

Remove cases for node:

1. Empty tree
2. Delete at root node
3. Value not in tree
4. Has left child only
5. Has right child only
6. Has both left and right child

"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    '''
    def __repr__(self):
    if self:
        return "{} / {} \ {}".format(self.rightChild, self.value, self.leftChild)
    '''

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
            print(str(self.value), end=", ")
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
            print("Pre order:", end=" ")
            self.root.preorder()
            print("\n")

    def postorder(self):
        if self.root is not None:
            print("Post order:", end=" ")
            self.root.postorder()
            print("\n")

    def inorder(self):
        if self.root is not None:
            print("In order:", end=" ")
            self.root.inorder()
            print("\n")

    def remove(self, data):
        """
        Remove has to handle 3 cases, like
        1. Deletion at Root Node
        2. Deletion of node having no children
        3. Deletion of node having 1 children
        4. Deletion of node having 2 children
        """
        # If empty tree return 'False'
        if self.root is None:
            return False

        # Deletion at root node
        elif self.root.value == data:
            if self.root.leftChild and self.root.rightChild is None:
                self.root = None
            elif self.leftChild and self.rightChild is None:
                self.root = self.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value

                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None

            return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild


        # case 1: data not found
        if node is None and node.value != data:
            return False

        # case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None

            return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild

            return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent, delNode = node, node.rightChild
            while delNode.leftChild:
                delNodeParent, delNode = delNode, delNode.leftChild

            node.value = delNode.value

            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None


if __name__ == "__main__":


        bst = Tree()
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
        bst.remove(9)

        #bst.postorder()
        #bst.preorder()
        bst.inorder()

