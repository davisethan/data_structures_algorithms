from data_structures.doubly_linked_list.doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode


class LfuCache:
    """
    least frequently used cache
    """
    def __init__(self, capacity=float("inf")):
        self.capacity = capacity
        self.size = 0
        self.indexer = dict()
        self.store = dict()
        self.minimum_frequency = 0

    def get(self, key):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if key not in self.indexer:
            return -1

        node = self.indexer[key]
        self.bump_frequency(node)
        return node.data.value

    def put(self, key, value):
        """
        time complexity O(1)
        space complexity O(1)
        """
        if key in self.indexer:
            node = self.indexer[key]
            self.bump_frequency(node)
            node.data.value = value
        else:
            # nonexistent node past capacity
            if self.size == self.capacity:
                node = self.store[self.minimum_frequency].pop()
                self.indexer.pop(node.data.key)
                self.size = self.size - 1

            # nonexistent node not past capacity
            self.minimum_frequency = 1
            if self.minimum_frequency not in self.store:
                self.store[self.minimum_frequency] = DoublyLinkedList()
            data = LfuCacheData(key, value, self.minimum_frequency)
            node = DoublyLinkedListNode(data)
            self.indexer[key] = node
            self.store[self.minimum_frequency].push(node)
            self.size = self.size + 1

    def bump_frequency(self, node):
        """
        time complexity O(1)
        space complexity O(1)
        """
        old_frequency = node.data.frequency
        new_frequency = node.data.frequency + 1

        # old frequency store is empty
        self.store[old_frequency].pop(node)
        if self.store[old_frequency].empty():
            self.store.pop(old_frequency)
            if self.minimum_frequency == old_frequency:
                self.minimum_frequency = new_frequency

        # new frequency store is empty
        node.data.frequency = new_frequency
        if new_frequency not in self.store:
            self.store[new_frequency] = DoublyLinkedList()
        self.store[new_frequency].push(node)

    def __repr__(self):
        result = list()
        for key in reversed(sorted(self.store.keys())):
            for node in self.store[key]:
                result.append(node)
        return str(result)


class LfuCacheData:
    def __init__(self, key, value, frequency):
        self.key = key
        self.value = value
        self.frequency = frequency

    def __repr__(self):
        return str((self.key, self.value, self.frequency))
