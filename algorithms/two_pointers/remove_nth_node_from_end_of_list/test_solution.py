"""
unit tests
"""

from unittest import TestCase
from algorithms.two_pointers.remove_nth_node_from_end_of_list.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_remove_first_node(self):
        # Given
        data = [15, -8, 3, -12, 7, -1, 19, -16, 10, -5]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        n = 1
        solution = Solution()

        # When
        head = solution.remove_nth_last_node(linked_list.head, n)
        result = LinkedList(head)
        actual = str(result)

        # Then
        expected = str([-5, 10, -16, 19, -1, 7, -12, 3, -8])
        self.assertEqual(actual, expected)

    def test_remove_middle_node(self):
        # Given
        data = [15, -8, 3, -12, 7, -1, 19, -16, 10, -5]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        n = 5
        solution = Solution()

        # When
        head = solution.remove_nth_last_node(linked_list.head, n)
        result = LinkedList(head)
        actual = str(result)

        # Then
        expected = str([-5, 10, -16, 19, -1, -12, 3, -8, 15])
        self.assertEqual(actual, expected)

    def test_remove_last_node(self):
        # Given
        data = [15, -8, 3, -12, 7, -1, 19, -16, 10, -5]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        n = 10
        solution = Solution()

        # When
        head = solution.remove_nth_last_node(linked_list.head, n)
        result = LinkedList(head)
        actual = str(result)

        # Then
        expected = str([10, -16, 19, -1, 7, -12, 3, -8, 15])
        self.assertEqual(actual, expected)
