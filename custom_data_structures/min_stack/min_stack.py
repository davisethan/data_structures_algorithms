from data_structures.stack.stack import Stack

class MinStack:
    def __init__(self):
        self.values = Stack()
        self.minimums = Stack()

    def push(self, value):
        self.values.push(value)
        if self.minimums.empty() or value < self.minimums.top():
            self.minimums.push(value)
        else:
            self.minimums.push(self.minimums.top())

    def pop(self):
        self.minimums.pop()
        return self.values.pop()

    def min_number(self):
        return self.minimums.top()

    def __repr__(self):
        return str(self.values)
