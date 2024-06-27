"""
unit tests
"""

from unittest import TestCase
from algorithms.counters.maximum_frequency_stack.frequency_stack import FrequencyStack


class FrequencyStackTestCase(TestCase):
    def test_push(self):
        # Given
        elements = [1, 3, 3, 5, 5, 5, 7, 7, 7, 7, 9, 9, 9, 9, 9]
        frequency_stack = FrequencyStack()

        # When
        [frequency_stack.push(element) for element in elements]
        actual = str(frequency_stack)

        # Then
        expected = str([[1, 3, 5, 7, 9], [3, 5, 7, 9], [5, 7, 9], [7, 9], [9]])
        self.assertEqual(actual, expected)

    def test_pop(self):
        # Given
        elements = [1, 3, 3, 5, 5, 5, 7, 7, 7, 7, 9, 9, 9, 9, 9]
        frequency_stack = FrequencyStack()
        [frequency_stack.push(element) for element in elements]

        # When
        actual = [frequency_stack.pop() for _ in range(len(elements))]

        # Then
        expected = [9, 9, 7, 9, 7, 5, 9, 7, 5, 3, 9, 7, 5, 3, 1]
        self.assertEqual(actual, expected)
