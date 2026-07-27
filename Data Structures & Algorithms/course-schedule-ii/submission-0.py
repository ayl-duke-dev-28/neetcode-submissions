from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):

        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visiting = set()
        visited = set()

        order = []

        def dfs(course):

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            visiting.remove(course)
            visited.add(course)

            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[::-1]