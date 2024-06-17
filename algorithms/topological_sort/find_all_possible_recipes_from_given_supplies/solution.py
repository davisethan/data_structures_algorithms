"""
production algorithm
"""

from collections import defaultdict
from data_structures.queue.queue import Queue


class Solution:
    def find_recipes(self, recipes, ingredients, supplies):
        """
        time complexity O(V + E)
        space complexity O(V + E)
        """
        # initialize graph vertexes
        graph = defaultdict(list)
        for recipe in recipes:
            graph[recipe]
        for recipe in ingredients:
            for ingredient in recipe:
                graph[ingredient]

        # initialize graph edges
        n = len(recipes)
        for i in range(n):
            recipe = recipes[i]
            m = len(ingredients[i])
            for j in range(m):
                ingredient = ingredients[i][j]
                graph[ingredient].append(recipe)

        # initialize indegree counter
        indegree = defaultdict(int)
        for v in graph:
            indegree[v]
            for u in graph[v]:
                indegree[u] += 1

        # initialize bfs queue
        queue = Queue()
        for v in indegree:
            if indegree[v] == 0 and v in supplies:
                queue.push(v)

        # sort
        result = list()
        while not queue.empty():
            v = queue.pop()
            if v in recipes:
                result.append(v)
            for u in graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.push(u)

        return result
