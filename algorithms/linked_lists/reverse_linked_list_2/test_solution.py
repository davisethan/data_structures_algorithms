"""
unit tests
"""

from unittest import TestCase
from algorithms.linked_lists.reverse_linked_list_2.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_reverse_between(self):
        # Given
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        left, right = 5, 10
        solution = Solution()

        # When
        head = solution.reverse_between(linked_list.head.next, left, right)
        reversed_linked_list = LinkedList()
        reversed_linked_list.head.next = head
        actual = str(reversed_linked_list)

        # Then
        expected = str([30, 28, 26, 24, 12, 14, 16,
                       18, 20, 22, 10, 8, 6, 4, 2])
        self.assertEqual(actual, expected)
