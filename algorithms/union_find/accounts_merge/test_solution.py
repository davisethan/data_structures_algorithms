"""
unit test
"""

from unittest import TestCase
from algorithms.union_find.accounts_merge.solution import Solution


class SolutionTestCase(TestCase):
    def test_zero_unions(self):
        # Given
        accounts = [["alice", "alice1@email.com", "alice3@email.com", "alice5@email.com"],
                    ["bob", "bob2@email.com", "bob4@email.com", "bob6@email.com"],
                    ["charlie", "charlie3@email.com", "charlie6@email.com", "charlie9@email.com"]]
        solution = Solution()

        # When
        actual = solution.accounts_merge(accounts)

        # Then
        expected = [["alice", "alice1@email.com", "alice3@email.com", "alice5@email.com"],
                    ["bob", "bob2@email.com", "bob4@email.com", "bob6@email.com"],
                    ["charlie", "charlie3@email.com", "charlie6@email.com", "charlie9@email.com"]]
        self.assertEqual(actual, expected)

    def test_unions_to_one_account(self):
        # Given
        accounts = [["alice", "alice1@email.com", "alice3@email.com", "alice5@email.com"],
                    ["alice", "alice3@email.com",
                        "alice6@email.com", "alice9@email.com"],
                    ["alice", "alice5@email.com", "alice10@email.com", "alice15@email.com"]]
        solution = Solution()

        # When
        actual = solution.accounts_merge(accounts)

        # Then
        expected = [["alice", "alice10@email.com", "alice15@email.com", "alice1@email.com",
                     "alice3@email.com", "alice5@email.com", "alice6@email.com", "alice9@email.com"]]
        self.assertEqual(actual, expected)

    def test_unions_to_many_accounts(self):
        # Given
        accounts = [["alice", "alice1@email.com", "alice3@email.com", "alice5@email.com"],
                    ["bob", "bob2@email.com", "bob4@email.com", "bob6@email.com"],
                    ["charlie", "charlie3@email.com",
                        "charlie6@email.com", "charlie9@email.com"],
                    ["alice", "alice5@email.com",
                        "alice7@email.com", "alice9@email.com"],
                    ["bob", "bob6@email.com", "bob8@email.com", "bob10@email.com"],
                    ["charlie", "charlie9@email.com", "charlie11@email.com", "charlie13@email.com"]]
        solution = Solution()

        # When
        actual = solution.accounts_merge(accounts)

        # Then
        expected = [["alice", "alice1@email.com", "alice3@email.com", "alice5@email.com", "alice7@email.com", "alice9@email.com"],
                    ["bob", "bob10@email.com", "bob2@email.com",
                        "bob4@email.com", "bob6@email.com", "bob8@email.com"],
                    ["charlie", "charlie11@email.com", "charlie13@email.com", "charlie3@email.com", "charlie6@email.com", "charlie9@email.com"]]
        self.assertEqual(actual, expected)
