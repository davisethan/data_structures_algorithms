"""
unit tests
"""

from unittest import TestCase
from algorithms.stacks.implement_queue_using_stacks.custom_queue import CustomQueue


class CustomQueueTestCase(TestCase):
    def test_push(self):
        # Given
        queue = CustomQueue()
        numbers = [1, 3, 5, 7, 9]

        # When
        [queue.push(number) for number in numbers]
        actual = queue.stack1.list

        # Then
        expected = [9, 7, 5, 3, 1]
        self.assertEqual(actual, expected)

    def test_pop(self):
        # Given
        queue = CustomQueue()
        numbers = [1, 3, 5, 7, 9]
        [queue.push(number) for number in numbers]

        # When
        actual = [queue.pop() for _ in range(len(numbers))]

        # Then
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(actual, expected)

    def test_peek(self):
        # Given
        queue = CustomQueue()
        numbers = [1, 3, 5, 7, 9]
        [queue.push(number) for number in numbers]

        # When
        actual = queue.peek()

        # Then
        expected = 1
        self.assertEqual(actual, expected)

    def test_empty(self):
        # Given
        queue = CustomQueue()

        # When
        actual = queue.empty()

        # Then
        expected = True
        self.assertEqual(actual, expected)
