from heapq import heappush, heappop


class Heap:
    def __init__(self):
        self.heap = list()

    def push(self, data):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        heappush(self.heap, data)

    def pop(self):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        return heappop(self.heap)

    def top(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.heap[0]

    def size(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return len(self.heap)

    def empty(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.size() == 0

    def __repr__(self):
        return str(sorted(self.heap))
