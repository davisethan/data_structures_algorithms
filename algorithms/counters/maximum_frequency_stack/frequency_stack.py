"""
production algorithm
"""

from collections import defaultdict


class FrequencyStack:
    def __init__(self):
        self.frequencies = defaultdict(int)
        self.stacks = []

    def push(self, value):
        """
        time complexity O(1)
        space complexity O(n)
        """
        self.frequencies[value] += 1
        if len(self.stacks) < self.frequencies[value]:
            self.stacks.append([])
        self.stacks[self.frequencies[value] - 1].append(value)

    def pop(self):
        """
        time complexity O(1)
        space complexity O(n)
        """
        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        self.frequencies[value] -= 1
        return value

    def __repr__(self):
        return str(self.stacks)
