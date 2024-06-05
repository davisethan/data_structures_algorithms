"""
production algorithm
"""


class Solution:
    def __init__(self, api):
        self.api = api

    def first_bad_version(self, n):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        low, high = 1, n
        count = 0

        while low <= high:
            mid = (high + low) // 2
            count += 1

            if self.is_bad_version(mid):
                high = mid - 1
            else:
                low = mid + 1

        return [low, count]

    def is_bad_version(self, version):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.api.call(version)


class API:
    def __init__(self, first_bad_version=0):
        self.first_bad_version = first_bad_version

    def call(self, version):
        return self.first_bad_version <= version
