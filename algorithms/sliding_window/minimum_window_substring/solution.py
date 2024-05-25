"""
production algorithm
"""

from collections import defaultdict, Counter


class Solution:
    def minimum_window_substring(self, string1, string2):
        """
        time complexity O(n)
        space complexity O(1)
        """
        if len(string1) < len(string2):
            return str()

        m, n = len(string1), len(string2)
        low, high = 0, 0
        frequencies, visited, total = Counter(string2), defaultdict(int), 0
        length, result = float("inf"), str()

        # step foward high index
        for high in range(m):
            if string1[high] in frequencies:
                if visited[string1[high]] < frequencies[string1[high]]:
                    total += 1
                visited[string1[high]] += 1

            # found match
            if total == n:

                # step forward low index
                while total == n:
                    if string1[low] in frequencies:
                        if visited[string1[low]] == frequencies[string1[low]]:
                            total -= 1
                        visited[string1[low]] -= 1
                    low += 1

                # found local minimum window substring match
                if high - low + 2 < length:
                    length = high - low + 2
                    result = string1[low-1:high+1]

        return result
