"""
production algorithm
"""

from collections import Counter
from data_structures.heap.heap import Heap


class Solution:
    def reorganize_string(self, string):
        """
        time complexity O(n)
        space complexity O(1)
        """
        length = len(string)
        largest = Heap()
        counter = Counter(string)
        [largest.push(MaxHeapData(counter[character], character))
         for character in counter]
        previous, result = [], []

        for _ in range(length):
            if largest.empty():
                break

            # add current character to result
            count, character = largest.pop()
            result.append(character)

            # add previous character back to choices
            if previous:
                largest.push(MaxHeapData(previous[0], previous[1]))
                previous = []

            # save current character as previous character
            if 0 < count - 1:
                previous = [count - 1, character]

        if len(result) < length:
            return str()
        return str().join(result)


class MaxHeapData:
    def __init__(self, count, character):
        self.count = count
        self.character = character

    def __lt__(self, other):
        if self.count == other.count:
            return self.character < other.character
        return other.count < self.count

    def __iter__(self):
        yield self.count
        yield self.character

    def __len__(self):
        return 2
