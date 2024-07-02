"""
unit tests
"""

from unittest import TestCase
from algorithms.fast_and_slow_pointers.linked_list_cycle.solution import Solution
from data_structures.linked_list.linked_list import LinkedList, LinkedListNode


class SolutionTestCase(TestCase):
    def test_linked_list_cycle_nonexistent(self):
        # Given
        data = [6, -9, 0, -8, 20, -2, -5, 16, 9, -18]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        actual = solution.detect_cycle(linked_list.head)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_linked_list_cycle_existent(self):
        # Given
        head, tail = LinkedListNode(-10), LinkedListNode(10)
        data = [6, -9, 0, -8, 20, -2, -5, 16, 9, -18]
        linked_list = LinkedList(tail)
        [linked_list.push(value) for value in data]
        linked_list.push(head.data)
        tail.next = linked_list.head
        solution = Solution()

        # When
        actual = solution.detect_cycle(linked_list.head)

        # Then
        expected = True
        self.assertEqual(actual, expected)
