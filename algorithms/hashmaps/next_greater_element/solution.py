"""
production algorithm
"""

from data_structures.stack.stack import Stack


class Solution:
    def next_greater_element(self, n1, n2):
        """
        time complexity O(n)
        space complexity O(n)
        """
        stack, hashmap = Stack(), dict()
        stack.push(n2[0])
        hashmap[n2[0]] = -1

        for i in range(1, len(n2)):
            while not stack.empty() and stack.top() < n2[i]:
                number = stack.pop()
                hashmap[number] = n2[i]
            stack.push(n2[i])
            hashmap[n2[i]] = -1

        result = [hashmap[n1[i]] for i in range(len(n1))]
        return result
