#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(set)

        def dfs(point, target,  visited):
            if target in graph[point]:
                return True
            for node in graph[point]:
                if node not in visited and dfs(node, target, visited | {point}):
                    return True
            return False
        for p1, p2 in edges:
            if dfs(p1, p2, set()):
                return [p1, p2]
            graph[p1].add(p2)
            graph[p2].add(p1)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        graph = defaultdict(set)

        def bfs(point, target):
            queue, visited = deque([point]), set()
            while queue:
                node = queue.popleft()
                visited.add(node)
                if target in graph[node]:
                    return True
                queue.extend(graph[node]-visited)
            return False
        for p1, p2 in edges:
            if bfs(p1, p2):
                return [p1, p2]
            graph[p1].add(p2)
            graph[p2].add(p1)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(set)

        def bfs(point, target):
            queue, visited = {point}, set()
            while queue:
                node = queue.pop()
                visited.add(node)
                if target in graph[node]:
                    return True
                queue |= graph[node]-visited
            return False
        for p1, p2 in edges:
            if bfs(p1, p2):
                return [p1, p2]
            graph[p1].add(p2)
            graph[p2].add(p1)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        f = dict()

        def find(x: int) -> int:
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x: int, y: int):
            f[find(x)] = f[find(y)]

        for p1, p2 in edges:
            if find(p1) == find(p2):
                return [p1, p2]
            union(p1, p2)


# @lc code=end
