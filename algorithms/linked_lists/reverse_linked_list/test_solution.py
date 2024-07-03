"""
unit tests
"""

from unittest import TestCase
from algorithms.linked_lists.reverse_linked_list.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_single_node_linked_list(self):
        # Given
        data = [1]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        head = solution.reverse(linked_list.head)
        reversed_linked_list = LinkedList()
        reversed_linked_list.push(head)
        actual = str(reversed_linked_list)

        # Then
        expected = str(data)
        self.assertEqual(actual, expected)

    def test_multiple_node_linked_list(self):
        # Given
        data = [1, 3, 5, 7, 9]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        head = solution.reverse(linked_list.head.next)
        reversed_linked_list = LinkedList()
        reversed_linked_list.head.next = head
        actual = str(reversed_linked_list)

        # Then
        expected = str(data)
        self.assertEqual(actual, expected)
