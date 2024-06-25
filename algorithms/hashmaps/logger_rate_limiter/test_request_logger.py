"""
unit tests
"""

from unittest import TestCase
from algorithms.hashmaps.logger_rate_limiter.request_logger import RequestLogger


class RequestLoggerTestCase(TestCase):
    def test_decision_is_false(self):
        # Given
        limit = 5
        logger = RequestLogger(limit)
        messages = [(1, "Hello"), (2, "Hello"), (3, "Hello"),
                    (4, "Hello"), (5, "Hello")]

        # When
        actual = [logger.message_request_decision(
            timestamp, message) for timestamp, message in messages]

        # Then
        expected = [True, False, False, False, False]
        self.assertEqual(actual, expected)

    def test_decision_is_true(self):
        # Given
        limit = 5
        logger = RequestLogger(limit)
        messages = [(10, "Hello"), (20, "Hello"), (30, "Hello"),
                    (40, "Hello"), (50, "Hello")]

        # When
        actual = [logger.message_request_decision(
            timestamp, message) for timestamp, message in messages]

        # Then
        expected = [True, True, True, True, True]
        self.assertEqual(actual, expected)
