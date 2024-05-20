from data_structures.doubly_linked_list.doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode


class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.indexer = dict()
        self.doubly_linked_list = DoublyLinkedList()

    def get(self, key):
        if key not in self.indexer:
            return -1
        node = self.indexer[key]
        self.doubly_linked_list.pop(node)
        self.doubly_linked_list.push(node)
        return node.data.value

    def set(self, key, value):
        if key in self.indexer:
            node = self.indexer[key]
            node.data.value = value
            self.doubly_linked_list.pop(node)
            self.doubly_linked_list.push(node)
        else:
            if self.doubly_linked_list.size == self.capacity:
                node = self.doubly_linked_list.pop()
                self.indexer.pop(node.data.key)
            data = LruCacheData(key, value)
            node = DoublyLinkedListNode(data)
            self.indexer[key] = node
            self.doubly_linked_list.push(node)

    def __repr__(self):
        return str(self.doubly_linked_list)


class LruCacheData:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str((self.key, self.value))
