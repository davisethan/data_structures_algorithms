"""
unit tests
"""

from unittest import TestCase
from algorithms.two_heaps.data_stream_median.data_stream_median import DataStreamMedian


class DataStreamMedianTestCase(TestCase):
    def test_insert_strictly_increasing_odd_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_maxheap = [55, 53, 51]
        expected_minheap = [57, 59]
        expected = f"(maxheap={expected_maxheap}, minheap={expected_minheap})"
        self.assertEqual(actual, expected)

    def test_median_strictly_increasing_odd_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 55
        self.assertEqual(actual, expected)

    def test_insert_strictly_decreasing_odd_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [59, 57, 55, 53, 51]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_maxheap = [55, 53, 51]
        expected_minheap = [57, 59]
        expected = f"(maxheap={expected_maxheap}, minheap={expected_minheap})"
        self.assertEqual(actual, expected)

    def test_median_strictly_decreasing_odd_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [59, 57, 55, 53, 51]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 55
        self.assertEqual(actual, expected)

    def test_insert_stricly_increasing_even_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59, 61]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_maxheap = [55, 53, 51]
        expected_minheap = [57, 59, 61]
        expected = f"(maxheap={expected_maxheap}, minheap={expected_minheap})"
        self.assertEqual(actual, expected)

    def test_median_stricly_increasing_even_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59, 61]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 56
        self.assertEqual(actual, expected)

    def test_insert_strictly_decreasing_even_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [61, 59, 57, 55, 53, 51]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_maxheap = [55, 53, 51]
        expected_minheap = [57, 59, 61]
        expected = f"(maxheap={expected_maxheap}, minheap={expected_minheap})"
        self.assertEqual(actual, expected)

    def test_median_striclty_decreasing_even_parity_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [61, 59, 57, 55, 53, 51]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 56
        self.assertEqual(actual, expected)
