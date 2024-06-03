"""
production algorithm
"""

from collections import Counter
from data_structures.heap.heap import Heap


class Solution:
    def top_k_frequent(self, words, k):
        """
        time complexity XXX
        space complexity XXX
        """
        smallest = Heap()
        counter = Counter(words)

        for word, frequency in counter.items():
            smallest.push(MinHeapData(frequency, word))
            if k < smallest.size():
                smallest.pop()

        return [smallest.pop().word for i in range(k)][::-1]


class MinHeapData:
    def __init__(self, frequency, word):
        self.frequency = frequency
        self.word = word

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return other.word < self.word
        return self.frequency < other.frequency
