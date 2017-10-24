"""
Implementation of Binary Tree and Traversals: Iterative way
"""


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def postorder(self, A):
        if A is None:
            return False

        stack = [(False, A)]
        result = []

        while stack:
            flag, val = stack.pop()
            if val:
                if not flag:
                    stack.append((True, val))
                    stack.append((False, val.right))
                    stack.append((False, val.left))
                else:
                    result.append(val.value)

        return result

    def preorder(self, A):
        if A is None:
            return False

        stack = [(False, A)]
        result = []

        while stack:
            flag, val = stack.pop()
            if val:
                if not flag:
                    stack.append((False, val.right))
                    stack.append((False, val.left))
                    stack.append((True, val))
                else:
                    result.append(val.value)

        return result


    def inorder(self, A):
        if A is None:
            return False
        stack = [(False, A)]
        result = []

        while stack:
            flag, val = stack.pop()

            if val:
                if not flag:
                    stack.append((False, val.right))
                    stack.append((True, val))
                    stack.append((False, val.left))
                else:
                    result.append(val.value)

        return result

    def levelorder(self, A):
        """
        Horizontal level order traversal
        :param A root node:
        :return array of values in level order traversal - horizontal:
        """
        if A is None:
            return False

        queue =[]
        queue.append(A)

        result = []

        while queue:
            result.append(queue[0].value)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

if __name__ == "__main__":

        mytree1 = TreeNode(1)
        mytree2 = TreeNode(2)
        mytree3 = TreeNode(3)
        mytree4 = TreeNode(6)
        mytree5 = TreeNode(5)
        mytree6 = TreeNode(4)

        mytree1.left = mytree2
        mytree1.right = mytree3
        mytree3.right = mytree4
        mytree3.left = mytree5
        mytree2.left = mytree6

        print ("Post order Traversal:")
        print(Tree().postorder(mytree1))

        print("Pre order Traversal:")
        print(Tree().preorder(mytree1))

        print("In order Traversal: ")
        print(Tree().inorder(mytree1))

        print("Level order Traversal: ")
        print(Tree().levelorder(mytree1))
