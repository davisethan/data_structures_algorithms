"""
production algorithm
"""


class Solution:
    def minimum_window_subsequence(self, string1, string2):
        """
        time complexity O(mn)
        space complexity O(1)
        """
        m, n = len(string1), len(string2)
        i, j = 0, 0
        length, result = float("inf"), str()

        # step forward
        while i < m:
            if string2[j] == string1[i]:
                j = j + 1
            i = i + 1

            # found match
            if j == n:
                high = i
                i, j = i - 1, j - 1

                # step backward to start of match
                while 0 <= j:
                    if string2[j] == string1[i]:
                        j = j - 1
                    i = i - 1

                i, j = i + 1, j + 1
                low = i

                # found new minimum window subsequence match
                if high - low < length:
                    length, result = high - low, string1[low:high]

                i = i + 1

        return result
