from unittest import TestCase
from custom_data_structures.random_set.random_set import RandomSet


class RandomSetTestCase(TestCase):
    def test_insert_nonexistent(self):
        # Given
        random_set = RandomSet()
        values = [51, 53, 55, 57, 59]

        # When
        actual_return = [random_set.insert(value) for value in values]
        actual_random_set = str(random_set)

        # Then
        expected_return = [True, True, True, True, True]
        expected_random_set = "[(51, 0), (53, 1), (55, 2), (57, 3), (59, 4)]"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_random_set, expected_random_set)

    def test_insert_existent(self):
        # Given
        random_set = RandomSet()
        values = [51, 53, 55, 57, 59]
        [random_set.insert(value) for value in values]
        value = 53

        # When
        actual = random_set.insert(value)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_delete_nonexistent(self):
        # Given
        random_set = RandomSet()
        values = [51, 53, 55, 57, 59]
        [random_set.insert(value) for value in values]
        value = 61

        # When
        actual = random_set.delete(value)

        # Then
        expected = False
        self.assertEqual(actual, expected)

    def test_delete_existent(self):
        # Given
        random_set = RandomSet()
        values = [51, 53, 55, 57, 59]
        [random_set.insert(value) for value in values]
        value = 53

        # When
        actual_return = random_set.delete(value)
        actual_random_set = str(random_set)

        # Then
        expected_return = True
        expected_random_set = "[(51, 0), (59, 1), (55, 2), (57, 3)]"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_random_set, expected_random_set)
