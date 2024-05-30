"""
unit tests
"""

from unittest import TestCase
from algorithms.k_way_merge.merge_k_sorted_lists.solution import Solution
from data_structures.linked_list.linked_list import LinkedList


class SolutionTestCase(TestCase):
    def test_small_k(self):
        # Given
        list1, list2 = LinkedList(), LinkedList()
        [list1.push(data) for data in reversed([1, 3, 5, 7, 9])]
        [list2.push(data) for data in reversed([0, 2, 4, 6, 8])]
        lists = [list1, list2]
        solution = Solution()

        # When
        actual = solution.merge_k_lists(lists)

        # Then
        expected = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
        self.assertEqual(str(actual), expected)

    def test_large_k(self):
        # Given
        list1, list2, list3, list4, list5 = LinkedList(
        ), LinkedList(), LinkedList(), LinkedList(), LinkedList()
        [list1.push(data) for data in reversed([3, 8, 12, 19, 27, 35, 42])]
        [list2.push(data) for data in reversed([2, 9, 15, 22, 29, 36, 44])]
        [list3.push(data) for data in reversed([4, 10, 14, 20, 24, 32, 47])]
        [list4.push(data) for data in reversed([1, 7, 16, 21, 30, 37, 45])]
        [list5.push(data) for data in reversed([5, 11, 18, 25, 33, 38, 46])]
        lists = [list1, list2, list3, list4, list5]
        solution = Solution()

        # When
        actual = solution.merge_k_lists(lists)

        # Then
        expected = "[1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 27, 29, 30, 32, 33, 35, 36, 37, 38, 42, 44, 45, 46, 47]"
        self.assertEqual(str(actual), expected)
