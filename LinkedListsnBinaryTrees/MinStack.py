"""
Implementation of Min Stack

Approach: Maintain one more stack with all the minimum values stored in a stack
"""

'''
Solution1: Using one more stack 'minstack' with the minimum values stored in the stack

Time: O(n)
Space: O(n)
'''


class Stack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, item):
        if len(self.stack) == 0:
            self.stack.append(item)
            self.minstack.append(item)
        else:
            self.stack.append(item)
            if item < self.minstack[-1]:
                self.minstack.append(item)

    def pop(self):
        if len(self.stack) != 0:
            if self.stack[-1] == self.minstack[-1]:
                self.minstack.pop()
            self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def getMin(self):
        if len(self.minstack) == 0:
            return -1
        return self.minstack[-1]

    def printStack(self):
        return self.stack

    def printMinStack(self):
        return self.minstack


if __name__ == "__main__":

        a = Stack()
        a.push(10)
        a.push(5)
        a.push(8)
        a.push(13)
        a.push(2)
        a.push(9)
        a.push(1)
        print(a.printStack())
        print(a.printMinStack())
        print(a.getMin())
        a.pop()
        a.pop()
        a.pop()
        print(a.printStack())
        print(a.printMinStack())
