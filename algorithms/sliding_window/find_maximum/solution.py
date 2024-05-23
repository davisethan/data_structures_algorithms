"""
production algorithm
"""

from collections import deque


class Solution:
    def find_maximum(self, numbers, size):
        """
        time complexity O(n)
        space complexity O(k)
        """
        window = deque()
        result = list()

        # build window
        for index in range(size):
            self.cleanup(numbers, index, window)
            window.append(index)
        result.append(numbers[window[0]])

        # slide window
        for index in range(size, len(numbers)):
            if window[0] < index - size + 1:
                window.popleft()
            self.cleanup(numbers, index, window)
            window.append(index)
            result.append(numbers[window[0]])

        return result

    def cleanup(self, numbers, index, window):
        """
        time complexity O(k)
        space complexity O(1)
        """
        while window and numbers[window[-1]] < numbers[index]:
            window.pop()
