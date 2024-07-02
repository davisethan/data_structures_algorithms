"""
unit tests
"""

from unittest import TestCase
from algorithms.fast_and_slow_pointers.middle_of_linked_list.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_odd_number_of_nodes(self):
        # Given
        data = [-14, -11, -1, 1, 0, 9, -9, 7, 20]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        middle = solution.get_middle_node(linked_list.head)
        actual = middle.data

        # Then
        expected = 0
        self.assertEqual(actual, expected)

    def test_even_number_of_nodes(self):
        # Given
        data = [-14, -11, -1, 1, 0, 9, -9, 7, 20, -13]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        middle = solution.get_middle_node(linked_list.head)
        actual = middle.data

        # Then
        expected = 9
        self.assertEqual(actual, expected)
