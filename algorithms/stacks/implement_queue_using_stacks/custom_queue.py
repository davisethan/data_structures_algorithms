"""
production algorithm
"""

from data_structures.stack.stack import Stack


class CustomQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        """
        time complexity O(n)
        space complexity O(1)
        """
        if self.stack1.empty():
            self.stack1.push(x)
            return

        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        self.stack2.push(x)
        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

    def pop(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.stack1.pop()

    def peek(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.stack1.top()

    def empty(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.stack1.empty()
