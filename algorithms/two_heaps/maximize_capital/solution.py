"""
production algorithm
"""

from data_structures.heap.heap import Heap


class Solution:
    def maximum_capital(self, c, k, capitals, profits):
        n = len(capitals)
        min_capitals, max_profits = Heap(), Heap()
        result = c

        # sort project capitals lowest to highest
        for i in range(n):
            min_capitals.push(MinHeapData(capitals[i], i))

        for i in range(k):

            # sort available project profits highest to lowest
            while not min_capitals.empty() and min_capitals.top().capital <= result:
                _, index = min_capitals.pop()
                max_profits.push(MaxHeapData(profits[index]))

            # add maximum available profit to cumulative capital
            if max_profits.empty():
                return result
            profit = max_profits.pop().profit
            result = result + profit

        return result


class MinHeapData:
    def __init__(self, capital, index):
        self.capital = capital
        self.index = index

    def __lt__(self, other):
        return self.capital < other.capital

    def __iter__(self):
        yield self.capital
        yield self.index

    def __len__(self):
        return 2


class MaxHeapData:
    def __init__(self, profit):
        self.profit = profit

    def __lt__(self, other):
        return other.profit < self.profit
