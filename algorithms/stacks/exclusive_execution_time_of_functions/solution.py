"""
production algorithm
"""

from data_structures.stack.stack import Stack


class Solution:
    def exclusive_time(self, n, logs):
        """
        time complexity O(k * (logn + logt))
        space complexity O(k)
        """
        stack, result = Stack(), [0 for _ in range(n)]

        for string in logs:
            log = Log(string)
            if log.event == "start":
                stack.push(log)
            else:
                top = stack.pop()
                result[top.id] += log.timestamp - top.timestamp + 1
                if not stack.empty():
                    result[stack.top().id] -= log.timestamp - top.timestamp + 1

        return result


class Log:
    def __init__(self, log):
        id, event, timestamp = log.split(":")
        self.id = int(id)
        self.event = event
        self.timestamp = int(timestamp)
