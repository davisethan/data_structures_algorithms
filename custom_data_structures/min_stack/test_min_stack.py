from unittest import TestCase
from custom_data_structures.min_stack.min_stack import MinStack


class MinStackTestCase(TestCase):
    def test_pop_empty(self):
        # Given
        minstack = MinStack()

        # When
        actual = minstack.pop()

        # Then
        expected = None
        self.assertEqual(actual, expected)

    def test_min_empty(self):
        # Given
        minstack = MinStack()

        # When
        actual = minstack.min_number()

        # Then
        expected = None
        self.assertEqual(actual, expected)

    def test_push_push_push(self):
        # Given
        minstack = MinStack()
        values = [55, 53, 51]

        # When
        [minstack.push(value) for value in values]
        actual_minimum = minstack.min_number()
        actual_minstack = str(minstack)

        # Then
        expected_minimum = 51
        expected_minstack = "[51, 53, 55]"
        self.assertEqual(actual_minimum, expected_minimum)
        self.assertEqual(actual_minstack, expected_minstack)

    def test_push_push_pop(self):
        # Given
        minstack = MinStack()
        values = [55, 53, 51]

        # When
        [minstack.push(value) for value in values]
        minstack.pop()
        actual_minimum = minstack.min_number()
        actual_minstack = str(minstack)

        # Then
        expected_minimum = 53
        expected_minstack = "[53, 55]"
        self.assertEqual(actual_minimum, expected_minimum)
        self.assertEqual(actual_minstack, expected_minstack)
