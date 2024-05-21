class Stack:
    def __init__(self):
        self.list = list()

    def push(self, value):
        """
        time complexity O(1)
        space complexity O(1)
        """
        self.list.append(value)

    def pop(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if self.empty():
            return None
        return self.list.pop()

    def top(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if self.empty():
            return None
        return self.list[-1]

    def size(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return len(self.list)

    def empty(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.size() == 0

    def __repr__(self):
        return str([value for value in reversed(self.list)])
