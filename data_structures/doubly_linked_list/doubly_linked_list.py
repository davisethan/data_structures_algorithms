class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = DoublyLinkedListNode()
        self.tail = DoublyLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, node):
        prev = self.head
        next = self.head.next
        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node
        self.size = self.size + 1

    def pop(self, node=None):
        if not node:
            node = self.tail.prev
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size = self.size - 1
        return node
    
    def __iter__(self):
        return DoublyLinkedListIterator(self.head, self.tail)
    
    def __repr__(self):
        return str([node for node in self])

class DoublyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)
    
class DoublyLinkedListIterator:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.current = head.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is self.tail:
            raise StopIteration
        data = self.current
        self.current = self.current.next
        return data
