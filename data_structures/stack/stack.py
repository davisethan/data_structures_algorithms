class Stack:
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.empty():
            return None
        return self.list.pop()

    def top(self):
        if self.empty():
            return None
        return self.list[-1]

    def size(self):
        return len(self.list)

    def empty(self):
        return self.size() == 0

    def __repr__(self):
        return str([value for value in reversed(self.list)])
