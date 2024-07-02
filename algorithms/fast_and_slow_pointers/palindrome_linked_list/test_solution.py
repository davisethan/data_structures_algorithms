"""
unit tests
"""

from unittest import TestCase
from algorithms.fast_and_slow_pointers.palindrome_linked_list.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_odd_length_linked_list_is_palindrome_succeeds(self):
        # Given
        data = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        actual = solution.palindrome(linked_list.head.next)

        # Then
        expected = True
        self.assertEqual(actual, expected)
        self.assertEqual(str(linked_list), str(data))

    def test_even_length_linked_list_is_palindrome_succeeds(self):
        # Given
        data = [1, 3, 5, 7, 9, 9, 7, 5, 3, 1]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        actual = solution.palindrome(linked_list.head.next)

        # Then
        expected = True
        self.assertEqual(actual, expected)
        self.assertEqual(str(linked_list), str(data))

    def test_odd_length_linked_list_is_palindrome_fails(self):
        # Given
        data = [1, 3, 5, 7, 9, 11, -9, 7, 5, 3, 1]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        actual = solution.palindrome(linked_list.head.next)

        # Then
        expected = False
        self.assertEqual(actual, expected)
        self.assertEqual(str(linked_list), str(list(reversed(data))))

    def test_even_length_linked_list_is_palindrome_fails(self):
        # Given
        data = [1, 3, 5, 7, 9, -9, 7, 5, 3, 1]
        linked_list = LinkedList()
        [linked_list.push(value) for value in data]
        solution = Solution()

        # When
        actual = solution.palindrome(linked_list.head.next)

        # Then
        expected = False
        self.assertEqual(actual, expected)
        self.assertEqual(str(linked_list), str(list(reversed(data))))
