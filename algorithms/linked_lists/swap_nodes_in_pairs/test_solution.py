"""
unit tests
"""

from unittest import TestCase
from algorithms.linked_lists.swap_nodes_in_pairs.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_zero_length_linked_list(self):
        # Given
        linked_list = LinkedList()
        solution = Solution()

        # When
        actual = solution.swap_pairs(linked_list.head.next)

        # Then
        expected = None
        self.assertEqual(actual, expected)

    def test_one_length_linked_list(self):
        # Given
        data = [2]
        linked_list = LinkedList()
        linked_list.push(data[0])
        solution = Solution()

        # When
        head = solution.swap_pairs(linked_list.head.next)
        swapped_linked_list = LinkedList()
        swapped_linked_list.head.next = head
        actual = str(swapped_linked_list)

        # Then
        expected = str([2])
        self.assertEqual(actual, expected)

    def test_two_length_linked_list(self):
        # Given
        data = [2, 4]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        head = solution.swap_pairs(linked_list.head.next)
        swapped_linked_list = LinkedList()
        swapped_linked_list.head.next = head
        actual = str(swapped_linked_list)

        # Then
        expected = str([2, 4])
        self.assertEqual(actual, expected)

    def test_even_length_linked_list(self):
        # Given
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        head = solution.swap_pairs(linked_list.head.next)
        swapped_linked_list = LinkedList()
        swapped_linked_list.head.next = head
        actual = str(swapped_linked_list)

        # Then
        expected = str([30, 32, 26, 28, 22, 24, 18,
                       20, 14, 16, 10, 12, 6, 8, 2, 4])
        self.assertEqual(actual, expected)

    def test_odd_length_linked_list(self):
        # Given
        data = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        head = solution.swap_pairs(linked_list.head.next)
        swapped_linked_list = LinkedList()
        swapped_linked_list.head.next = head
        actual = str(swapped_linked_list)

        # Then
        expected = str([30, 32, 26, 28, 22, 24, 18,
                       20, 14, 16, 10, 12, 6, 8, 4])
        self.assertEqual(actual, expected)
