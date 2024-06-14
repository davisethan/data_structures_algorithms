"""
unit tests
"""

from unittest import TestCase
from algorithms.topological_sort.find_compilation_order.solution import Solution


class SolutionTestCase(TestCase):
    def test_list_like_dependencies(self):
        # Given
        dependencies = [("H", "G"), ("G", "F"), ("F", "E"),
                        ("E", "D"), ("D", "C"), ("C", "B"), ("B", "A")]
        solution = Solution()

        # When
        actual = solution.find_compilation_order(dependencies)

        # Then
        expected = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.assertEqual(actual, expected)

    def test_binary_tree_like_dependencies(self):
        # Given
        dependencies = [("H", "D"), ("D", "B"), ("B", "A"),
                        ("E", "B"), ("F", "C"), ("G", "C"), ("C", "A")]
        solution = Solution()

        # When
        actual = solution.find_compilation_order(dependencies)

        # Then
        expected = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.assertEqual(actual, expected)

    def test_graph_like_dependencies(self):
        # Given
        dependencies = [("H", "D"), ("D", "B"), ("D", "E"), ("E", "B"), ("E", "F"),
                        ("F", "C"), ("F", "G"), ("G", "C"), ("B", "A"), ("B", "C"),
                        ("C", "A")]
        solution = Solution()

        # When
        actual = solution.find_compilation_order(dependencies)

        # Then
        expected = ["A", "C", "G", "B", "F", "E", "D", "H"]
        self.assertEqual(actual, expected)
