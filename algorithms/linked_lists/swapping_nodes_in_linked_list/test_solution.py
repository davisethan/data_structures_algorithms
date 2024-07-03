"""
unit tests
"""

from unittest import TestCase
from algorithms.linked_lists.swapping_nodes_in_linked_list.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_zero_length_between_kth_and_kth_last(self):
        # Given
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        k = 8
        solution = Solution()

        # When
        head = solution.swap_nodes(linked_list.head.next, k)
        swapped_linked_list = LinkedList()
        swapped_linked_list.head.next = head
        actual = str(swapped_linked_list)

        # Then
        expected = str([30, 28, 26, 24, 22, 20, 18,
                       16, 14, 12, 10, 8, 6, 4, 2])
        self.assertEqual(actual, expected)

    def test_one_length_between_kth_and_kth_last(self):
        # Given
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        k = 7
        solution = Solution()

        # When
        head = solution.swap_nodes(linked_list.head.next, k)
        swapped_linked_list = LinkedList()
        swapped_linked_list.head.next = head
        actual = str(swapped_linked_list)

        # Then
        expected = str([30, 28, 26, 24, 22, 20, 14,
                       16, 18, 12, 10, 8, 6, 4, 2])
        self.assertEqual(actual, expected)

    def test_two_length_between_kth_and_kth_last(self):
        # Given
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        k = 6
        solution = Solution()

        # When
        head = solution.swap_nodes(linked_list.head.next, k)
        swapped_linked_list = LinkedList()
        swapped_linked_list.head.next = head
        actual = str(swapped_linked_list)

        # Then
        expected = str([30, 28, 26, 24, 22, 12, 18,
                       16, 14, 20, 10, 8, 6, 4, 2])
        self.assertEqual(actual, expected)
