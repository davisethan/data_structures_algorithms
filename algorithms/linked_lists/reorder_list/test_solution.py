"""
unit tests
"""

from unittest import TestCase
from algorithms.linked_lists.reorder_list.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_odd_length_linked_list(self):
        # Given
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        head = solution.reorder_list(linked_list.head.next)
        reordered_linked_list = LinkedList()
        reordered_linked_list.head.next = head
        actual = str(reordered_linked_list)

        # Then
        expected = str([30, 2, 28, 4, 26, 6, 24, 8,
                       22, 10, 20, 12, 18, 14, 16])
        self.assertEqual(actual, expected)

    def test_even_length_linked_list(self):
        # Given
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        head = solution.reorder_list(linked_list.head.next)
        reordered_linked_list = LinkedList()
        reordered_linked_list.head.next = head
        actual = str(reordered_linked_list)

        # Then
        expected = str([32, 2, 30, 4, 28, 6, 26, 8,
                       24, 10, 22, 12, 20, 14, 18, 16])
        self.assertEqual(actual, expected)
