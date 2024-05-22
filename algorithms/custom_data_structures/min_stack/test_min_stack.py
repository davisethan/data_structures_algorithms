from unittest import TestCase
from custom_data_structures.min_stack.min_stack import MinStack


class MinStackTestCase(TestCase):
    def test_pop_empty(self):
        # Given
        min_stack = MinStack()

        # When
        actual = min_stack.pop()

        # Then
        expected = None
        self.assertEqual(actual, expected)

    def test_min_empty(self):
        # Given
        min_stack = MinStack()

        # When
        actual = min_stack.min_number()

        # Then
        expected = None
        self.assertEqual(actual, expected)

    def test_push_push_push(self):
        # Given
        min_stack = MinStack()
        values = [55, 53, 51]

        # When
        [min_stack.push(value) for value in values]
        actual_minimum = min_stack.min_number()
        actual_min_stack = str(min_stack)

        # Then
        expected_minimum = 51
        expected_min_stack = "[51, 53, 55]"
        self.assertEqual(actual_minimum, expected_minimum)
        self.assertEqual(actual_min_stack, expected_min_stack)

    def test_push_push_pop(self):
        # Given
        min_stack = MinStack()
        values = [55, 53, 51]

        # When
        [min_stack.push(value) for value in values]
        min_stack.pop()
        actual_minimum = min_stack.min_number()
        actual_min_stack = str(min_stack)

        # Then
        expected_minimum = 53
        expected_min_stack = "[53, 55]"
        self.assertEqual(actual_minimum, expected_minimum)
        self.assertEqual(actual_min_stack, expected_min_stack)
