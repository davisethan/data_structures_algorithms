class LinkedList:
    def __init__(self, head=None):
        self.size = 0
        if head is None:
            head = LinkedListNode()
        self.head = head

    def push(self, data):
        """
        time complexity O(1)
        space complexity O(1)
        """
        node = LinkedListNode(data)
        node.next = self.head.next
        self.head.next = node
        self.size = self.size + 1

    def empty(self):
        """
        time complexity O(1)
        space complexity O(1)
        """
        return self.size == 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __repr__(self):
        return str([node for node in self])


class LinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class LinkedListIterator:
    def __init__(self, head):
        self.head = head
        self.current = head.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current
        self.current = self.current.next
        return data
