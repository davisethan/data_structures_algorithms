from unittest import TestCase
from custom_data_structures.timestamp_hashmap.timestamp_hashmap import TimeStampHashMap


class TimeStampHashMapTestCase(TestCase):
    def test_get_nonexistent_key(self):
        # Given
        timestamp_hashmap = TimeStampHashMap()
        key = 51
        timestamp = 151

        # When
        actual = timestamp_hashmap.get(key, timestamp)

        # Then
        expected = str()
        self.assertEqual(actual, expected)

    def test_set_nonexistent_key(self):
        # Given
        timestamp_hashmap = TimeStampHashMap()
        key = 51
        timestamp = 151
        value = 51

        # When
        timestamp_hashmap.set(key, value, timestamp)
        actual_timestamp_hashmap = str(timestamp_hashmap)

        # Then
        expected_timestamps = [(51, [151])]
        expected_values = [(51, 151, 51)]
        expected_timestamp_hashmap = f"(timestamps={expected_timestamps}, values={expected_values})"
        self.assertEqual(actual_timestamp_hashmap, expected_timestamp_hashmap)

    def test_set_existent_key(self):
        # Given
        timestamp_hashmap = TimeStampHashMap()
        keys_timestamps_values = [
            (51, 151, 51), (51, 153, 53), (51, 155, 55),
            (51, 157, 57), (51, 159, 59)
        ]

        # When
        [timestamp_hashmap.set(key, value, timestamp)
         for key, timestamp, value in keys_timestamps_values]
        actual_timestamp_hashmap = str(timestamp_hashmap)

        # Then
        expected_timestamps = [(51, [151, 153, 155, 157, 159])]
        expected_values = [(51, 151, 51), (51, 153, 53),
                           (51, 155, 55), (51, 157, 57), (51, 159, 59)]
        expected_timestamp_hashmap = f"(timestamps={expected_timestamps}, values={expected_values})"
        self.assertEqual(actual_timestamp_hashmap, expected_timestamp_hashmap)

    def test_get_invalid_timestamp(self):
        # Given
        timestamp_hashmap = TimeStampHashMap()
        keys_timestamps_values = [
            (51, 151, 51), (51, 153, 53), (51, 155, 55),
            (51, 157, 57), (51, 159, 59)
        ]
        [timestamp_hashmap.set(key, value, timestamp)
         for key, timestamp, value in keys_timestamps_values]
        key = 51
        timestamp = 141

        # When
        actual = timestamp_hashmap.get(key, timestamp)

        # Then
        expected = str()
        self.assertEqual(actual, expected)

    def test_get_exact_timestamp(self):
        # Given
        timestamp_hashmap = TimeStampHashMap()
        keys_timestamps_values = [
            (51, 151, 51), (51, 153, 53), (51, 155, 55),
            (51, 157, 57), (51, 159, 59), (51, 161, 61),
            (51, 163, 63), (51, 165, 65), (51, 167, 67),
            (51, 169, 69), (51, 171, 71), (51, 173, 73),
            (51, 175, 75), (51, 177, 77), (51, 179, 79),
            (51, 181, 81), (51, 183, 83), (51, 185, 85),
            (51, 187, 87), (51, 189, 89)
        ]
        [timestamp_hashmap.set(key, value, timestamp)
         for key, timestamp, value in keys_timestamps_values]
        key = 51
        timestamp = 185

        # When
        actual = timestamp_hashmap.get(key, timestamp)

        # Then
        expected = 85
        self.assertEqual(actual, expected)

    def test_get_nonexact_timestamp(self):
        # Given
        timestamp_hashmap = TimeStampHashMap()
        keys_timestamps_values = [
            (51, 151, 51), (51, 153, 53), (51, 155, 55),
            (51, 157, 57), (51, 159, 59), (51, 161, 61),
            (51, 163, 63), (51, 165, 65), (51, 167, 67),
            (51, 169, 69), (51, 171, 71), (51, 173, 73),
            (51, 175, 75), (51, 177, 77), (51, 179, 79),
            (51, 181, 81), (51, 183, 83), (51, 185, 85),
            (51, 187, 87), (51, 189, 89)
        ]
        [timestamp_hashmap.set(key, value, timestamp)
         for key, timestamp, value in keys_timestamps_values]
        key = 51
        timestamp = 184

        # When
        actual = timestamp_hashmap.get(key, timestamp)

        # Then
        expected = 83
        self.assertEqual(actual, expected)
