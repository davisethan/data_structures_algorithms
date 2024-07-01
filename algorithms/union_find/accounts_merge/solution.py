"""
production algorithm
"""


class Solution:
    def accounts_merge(self, accounts):
        """
        time complexity O(nklog(nk))
        space complexity O(nk)
        """
        size = len(accounts)
        unionfind = UnionFind(size)

        # build reverse index from email to account
        emails = {}
        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emails:
                    emails[email] = index
                else:
                    representative = unionfind.find(emails[email])
                    unionfind.union(index, representative)

        # merge accounts
        merged = [[] for _ in range(size)]
        for email, index in emails.items():
            representative = unionfind.find(index)
            if not merged[representative]:
                merged[representative] = [accounts[representative][0]]
            merged[representative].append(email)
        merged = [[account[0]] + sorted(account[1:])
                  for account in merged if account]
        return merged


class UnionFind:
    def __init__(self, size):
        self.parent = [n for n in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, x):
        """
        time complexity O(⍺(n))
        space complexity O(n)
        """
        if not self.parent[x] == x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        time complexity O(⍺(n))
        space complexity O(n)
        """
        rootx = self.find(x)
        rooty = self.find(y)
        if not rootx == rooty:
            if self.size[rootx] < self.size[rooty]:
                rooty, rootx = rootx, rooty
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
