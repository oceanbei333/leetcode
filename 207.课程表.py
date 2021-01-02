#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        degree = [0]*numCourses
        graph = defaultdict(list)
        for dest, source in prerequisites:
            graph[source].append(dest)
            degree[dest] += 1
        queue = [i for i in range(numCourses) if not degree[i]]
        result = 0
        while queue:
            source = queue.pop()
            result += 1
            for dest in graph[source]:
                degree[dest] -= 1
                if not degree[dest]:
                    queue.append(dest)
        return result == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for dest, source in prerequisites:
            graph[source].append(dest)
        visited = [0]*numCourses
        self.valid = True
        result = []

        def dfs(source: int):
            visited[source] = 1
            for dest in graph[source]:
                if not visited[dest]:
                    dfs(dest)
                    if not self.valid:
                        return
                elif visited[dest] == 1:
                    self.valid = False
                    return
            visited[source] == 2
            result.append(source)
        for source in range(numCourses):
            if self.valid and not visited[source]:
                dfs(source)
        return self.valid

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        self.valid = True

        from collections import defaultdict

        graph = defaultdict(list)
        for dest, source in prerequisites:
            graph[source].append(dest)

        def dfs(source: int):
            visited[source] = 1
            for dest in graph[source]:
                if not visited[dest]:
                    dfs(dest)
                elif visited[dest] == 1:
                    self.valid = False
                if not self.valid:
                    return
            visited[source] = 2

        for source in range(numCourses):
            if not visited[source]:
                dfs(source)
            if not self.valid:
                return False
        return True

# @lc code=end
