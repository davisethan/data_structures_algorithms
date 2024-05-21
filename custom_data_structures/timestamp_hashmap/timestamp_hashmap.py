class TimeStampHashMap:
    """
    store multiple values of the same key and
    retrieve the key value at a certain timestamp otherwise
    retrieve the key value at the most recent timestamp

    all timestamps received by the set operation are strictly increasing
    """

    def __init__(self):
        self.timestamps = dict()
        self.values = dict()

    def get(self, key, timestamp):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        if key not in self.timestamps:
            return str()
        if timestamp < self.timestamps[key][0]:
            return str()
        index = self.binary_search_nearest(self.timestamps[key], timestamp)
        return self.values[(key, self.timestamps[key][index])]

    def set(self, key, value, timestamp):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if key not in self.timestamps:
            self.timestamps[key] = list()
        self.timestamps[key].append(timestamp)
        self.values[(key, timestamp)] = value

    def binary_search_nearest(self, array, value):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        low = 0
        high = len(array) - 1
        index = 0
        return self.binary_search_nearest_helper(array, value, low, high, index)

    def binary_search_nearest_helper(self, array, value, low, high, index):
        """
        time complexity O(logn)
        space complexity O(1)
        """
        while low <= high:
            mid = (low + high) // 2
            if array[mid] == value:
                return mid
            if array[mid] < value:
                low = mid + 1
                index = mid
            else:
                high = mid - 1
        return index

    def __repr__(self):
        timestamps = [(key, self.timestamps[key])
                      for key in sorted(self.timestamps.keys())]
        values = [(key, timestamp, self.values[(key, timestamp)])
                  for key, timestamp in sorted(self.values.keys())]
        return f"(timestamps={timestamps}, values={values})"
