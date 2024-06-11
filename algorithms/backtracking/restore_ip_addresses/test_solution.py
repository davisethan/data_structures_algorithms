"""
unit tests
"""

from unittest import TestCase
from algorithms.backtracking.restore_ip_addresses.solution import Solution


class SolutionTestCase(TestCase):
    def test_minimum_ip_addresses(self):
        # Given
        string = "1111"
        solution = Solution()

        # When
        actual = solution.restore_ip_addresses(string)

        # Then
        expected = ["1.1.1.1"]
        self.assertEqual(actual, expected)

    def test_maximum_ip_addresses(self):
        # Given
        string = "255255255255"
        solution = Solution()

        # When
        actual = solution.restore_ip_addresses(string)

        # Then
        expected = ["255.255.255.255"]
        self.assertEqual(actual, expected)

    def test_multiple_solutions(self):
        # Given
        string = "19216811"
        solution = Solution()

        # When
        addresses = solution.restore_ip_addresses(string)
        actual = set(addresses)

        # Then
        expected = {"192.168.1.1", "192.16.81.1", "192.16.8.11", "192.1.68.11",
                    "19.21.68.11", "19.2.168.11", "1.92.168.11", "19.216.81.1",
                    "19.216.8.11"}
        self.assertEqual(actual, expected)

    def test_leading_zeros_prevented(self):
        # Given
        string = "1921681001"
        solution = Solution()

        # When
        actual = solution.restore_ip_addresses(string)

        # Then
        expected = ["192.168.100.1"]
        self.assertEqual(actual, expected)
