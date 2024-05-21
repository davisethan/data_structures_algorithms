from unittest import TestCase
from custom_data_structures.lfu_cache.lfu_cache import LfuCache


class LfuCacheTestCase(TestCase):
    def test_get_nonexistent(self):
        # Given
        capacity = 5
        lfu_cache = LfuCache(capacity)
        key = 51

        # When
        actual = lfu_cache.get(key)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_put_without_duplicates(self):
        # Given
        capacity = 5
        lfu_cache = LfuCache(capacity)
        keys_values = [(51, 51), (53, 53), (55, 55), (57, 57), (59, 59)]

        # When
        [lfu_cache.put(key, value) for key, value in keys_values]
        actual = str(lfu_cache)

        # Then
        expected = "[(59, 59, 1), (57, 57, 1), (55, 55, 1), (53, 53, 1), (51, 51, 1)]"
        self.assertEqual(actual, expected)

    def test_put_without_duplicates_past_capacity(self):
        # Given
        capacity = 5
        lfu_cache = LfuCache(capacity)
        keys_values = [(51, 51), (53, 53), (55, 55), (57, 57), (59, 59)]
        [lfu_cache.put(key, value) for key, value in keys_values]
        key = 61
        value = 61

        # When
        lfu_cache.put(key, value)
        actual = str(lfu_cache)

        # Then
        expected = "[(61, 61, 1), (59, 59, 1), (57, 57, 1), (55, 55, 1), (53, 53, 1)]"
        self.assertEqual(actual, expected)

    def test_get_existent(self):
        # Given
        capacity = 5
        lfu_cache = LfuCache(capacity)
        keys_values = [(51, 51), (53, 53), (55, 55), (57, 57), (59, 59)]
        [lfu_cache.put(key, value) for key, value in keys_values]
        key = 53

        # When
        actual_value = lfu_cache.get(key)
        actual_lfu_cache = str(lfu_cache)

        # Then
        expected_value = 53
        expected_lfu_cache = "[(53, 53, 2), (59, 59, 1), (57, 57, 1), (55, 55, 1), (51, 51, 1)]"
        self.assertEqual(actual_value, expected_value)
        self.assertEqual(actual_lfu_cache, expected_lfu_cache)

    def test_put_with_duplicates(self):
        # Given
        capacity = 5
        lfu_cache = LfuCache(capacity)
        keys_values = [
            (51, 51), (51, 71), (51, 71),
            (53, 53), (53, 73), (53, 73),
            (55, 55), (55, 75), (55, 75), (55, 75),
            (57, 57), (57, 77), (57, 77), (57, 77),
            (59, 59), (59, 79), (59, 79), (59, 79), (59, 79)]

        # When
        [lfu_cache.put(key, value) for key, value in keys_values]
        actual_lfu_cache = str(lfu_cache)

        # Then
        expected_lfu_cache = "[(59, 79, 5), (57, 77, 4), (55, 75, 4), (53, 73, 3), (51, 71, 3)]"
        self.assertEqual(actual_lfu_cache, expected_lfu_cache)

    def test_put_with_duplicates_past_capacity(self):
        # Given
        capacity = 5
        lfu_cache = LfuCache(capacity)
        keys_values = [
            (51, 51), (51, 71), (51, 71),
            (53, 53), (53, 73), (53, 73),
            (55, 55), (55, 75), (55, 75), (55, 75),
            (57, 57), (57, 77), (57, 77), (57, 77),
            (59, 59), (59, 79), (59, 79), (59, 79), (59, 79)]
        [lfu_cache.put(key, value) for key, value in keys_values]
        key = 91
        value = 91

        # When
        lfu_cache.put(key, value)
        actual_lfu_cache = str(lfu_cache)

        # Then
        expected_lfu_cache = "[(59, 79, 5), (57, 77, 4), (55, 75, 4), (53, 73, 3), (91, 91, 1)]"
        self.assertEqual(actual_lfu_cache, expected_lfu_cache)
