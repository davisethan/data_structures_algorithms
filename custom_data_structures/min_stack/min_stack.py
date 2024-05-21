from data_structures.stack.stack import Stack


class MinStack:
    """
    get minimum value of stack in time complexity O(1)
    """
    def __init__(self):
        self.values = Stack()
        self.minimums = Stack()

    def push(self, value):
        """
        time complexity O(1)
        space complexity O(1)
        """
        self.values.push(value)
        if self.minimums.empty() or value < self.minimums.top():
            self.minimums.push(value)
        else:
            self.minimums.push(self.minimums.top())

    def pop(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        self.minimums.pop()
        return self.values.pop()

    def min_number(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.minimums.top()

    def __repr__(self):
        return str(self.values)
