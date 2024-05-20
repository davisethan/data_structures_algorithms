from unittest import TestCase
from custom_data_structures.lru_cache.lru_cache import LruCache


class LruCacheTestCase(TestCase):
    def test_get_nonexistent(self):
        # Given
        capacity = 5
        lru_cache = LruCache(capacity)
        key = 51

        # When
        actual = lru_cache.get(key)

        # Then
        expected = -1
        self.assertEqual(actual, expected)

    def test_set_without_reorder(self):
        # Given
        capacity = 5
        lru_cache = LruCache(capacity)
        keys_values = [(51, 51), (53, 53), (55, 55), (57, 57), (59, 59)]

        # When
        [lru_cache.set(key, value) for key, value in keys_values]
        actual = str(lru_cache)

        # Then
        expected = "[(59, 59), (57, 57), (55, 55), (53, 53), (51, 51)]"
        self.assertEqual(actual, expected)

    def test_get_with_reorder(self):
        # Given
        capacity = 5
        lru_cache = LruCache(capacity)
        keys_values = [(51, 51), (53, 53), (55, 55), (57, 57), (59, 59)]
        [lru_cache.set(key, value) for key, value in keys_values]
        key = 53

        # When
        actual_value = lru_cache.get(key)
        actual_lru_cache = str(lru_cache)

        # Then
        expected_value = 53
        expected_lru_cache = "[(53, 53), (59, 59), (57, 57), (55, 55), (51, 51)]"
        self.assertEqual(actual_value, expected_value)
        self.assertEqual(actual_lru_cache, expected_lru_cache)

    def test_set_with_reorder(self):
        # Given
        capacity = 5
        lru_cache = LruCache(capacity)
        keys_values = [(51, 51), (53, 53), (55, 55), (57, 57), (59, 59)]
        [lru_cache.set(key, value) for key, value in keys_values]
        key = 53
        value = 35

        # When
        lru_cache.set(key, value)
        actual_lru_cache = str(lru_cache)

        # Then
        expected_lru_cache = "[(53, 35), (59, 59), (57, 57), (55, 55), (51, 51)]"
        self.assertEqual(actual_lru_cache, expected_lru_cache)

    def test_set_past_capacity(self):
        # Given
        capacity = 5
        lru_cache = LruCache(capacity)
        keys_values = [(51, 51), (53, 53), (55, 55), (57, 57), (59, 59)]
        [lru_cache.set(key, value) for key, value in keys_values]
        key = 61
        value = 61

        # When
        lru_cache.set(key, value)
        actual_lru_cache = str(lru_cache)

        # Then
        expected_lru_cache = "[(61, 61), (59, 59), (57, 57), (55, 55), (53, 53)]"
        self.assertEqual(actual_lru_cache, expected_lru_cache)
