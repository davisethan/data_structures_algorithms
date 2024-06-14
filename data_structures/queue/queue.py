from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, data):
        """
        time complexity O(1)
        space complexity O(1)
        """
        self.queue.append(data)

    def pop(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.queue.popleft()

    def peek(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.queue[0]

    def size(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return len(self.queue)

    def empty(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.size() == 0
