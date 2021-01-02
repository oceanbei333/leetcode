#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        degree = [0]*numCourses
        graph = defaultdict(list)
        for dest, source in prerequisites:
            graph[source].append(dest)
            degree[dest] += 1
        queue = [i for i in range(numCourses) if not degree[i]]
        result = []
        while queue:
            source = queue.pop()
            result.append(source)
            for dest in graph[source]:
                degree[dest] -= 1
                if not degree[dest]:
                    queue.append(dest)
        return result if len(result) == numCourses else []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        self.valid = True

        from collections import defaultdict
        result = []
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
            result.append(source)

        for source in range(numCourses):
            if not visited[source]:
                dfs(source)
            if not self.valid:
                return []
        return result[::-1]

# @lc code=end
