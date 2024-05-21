from random import choice


class RandomSet:
    """
    insert delete and get random value of set all in time complexity O(1)
    """
    def __init__(self):
        self.store = list()
        self.indexer = dict()

    def insert(self, value):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if value in self.indexer:
            return False
        self.store.append(value)
        index = len(self.store) - 1
        self.indexer[value] = index
        return True

    def delete(self, value):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if value not in self.indexer:
            return False
        index = self.indexer[value]
        self.store[index], self.store[-1] = self.store[-1], self.store[index]
        self.indexer[self.store[index]] = index
        self.store.pop()
        self.indexer.pop(value)
        return True

    def get_random(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return choice(self.store)

    def __repr__(self):
        visited = set()
        result = list()
        for index, value in enumerate(self.store):
            result.append((value, index))
            visited.add((value, index))
        for key, value in self.indexer.items():
            if (key, value) not in visited:
                result.append((key, value))
        return str(result)
