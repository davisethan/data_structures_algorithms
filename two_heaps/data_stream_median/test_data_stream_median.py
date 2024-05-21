from unittest import TestCase
from two_heaps.data_stream_median.data_stream_median import DataStreamMedian


class DataStreamMedianTestCase(TestCase):
    def test_insert_five_strictly_increasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_max_heap = [53, 51]
        expected_min_heap = [55, 57, 59]
        expected = f"(max_heap={expected_max_heap}, min_heap={expected_min_heap})"
        self.assertEqual(actual, expected)

    def test_median_five_strictly_increasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 55
        self.assertEqual(actual, expected)

    def test_insert_five_strictly_decreasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [59, 57, 55, 53, 51]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_max_heap = [55, 53, 51]
        expected_min_heap = [57, 59]
        expected = f"(max_heap={expected_max_heap}, min_heap={expected_min_heap})"
        self.assertEqual(actual, expected)

    def test_median_five_strictly_decreasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [59, 57, 55, 53, 51]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 55
        self.assertEqual(actual, expected)

    def test_insert_six_stricly_increasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59, 61]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_max_heap = [55, 53, 51]
        expected_min_heap = [57, 59, 61]
        expected = f"(max_heap={expected_max_heap}, min_heap={expected_min_heap})"
        self.assertEqual(actual, expected)

    def test_median_six_stricly_increasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [51, 53, 55, 57, 59, 61]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 56
        self.assertEqual(actual, expected)

    def test_insert_six_strictly_decreasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [61, 59, 57, 55, 53, 51]

        # When
        [data_stream_median.insert(number) for number in numbers]
        actual = str(data_stream_median)

        # Then
        expected_max_heap = [55, 53, 51]
        expected_min_heap = [57, 59, 61]
        expected = f"(max_heap={expected_max_heap}, min_heap={expected_min_heap})"
        self.assertEqual(actual, expected)

    def test_median_six_striclty_decreasing_numbers(self):
        # Given
        data_stream_median = DataStreamMedian()
        numbers = [61, 59, 57, 55, 53, 51]
        [data_stream_median.insert(number) for number in numbers]

        # When
        actual = data_stream_median.median()

        # Then
        expected = 56
        self.assertEqual(actual, expected)
