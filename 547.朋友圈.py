#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
import functools
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        f = dict()
        self.result = len(M)

        def find(x: int) -> int:
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x: int, y: int):
            x_parent, y_parent = find(x), find(y)
            if x_parent == y_parent:
                return
            f[x_parent] = y_parent
            self.result -= 1
        for x in range(len(M)):
            for y in range(x+1, len(M)):
                if M[x][y]:
                    union(x, y)
        return self.result

    def findCircleNum(self, M: List[List[int]]) -> int:
        length = len(M)
        f = list(range(length))

        def find(x: int) -> int:
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x: int, y: int):
            x_parent, y_parent = find(x), find(y)
            if x_parent == y_parent:
                return
            f[x_parent] = y_parent
        for x in range(length):
            for y in range(x+1, length):
                if M[x][y]:
                    union(x, y)
        for x in range(length):
            find(x)
        return len(set(f))

    def findCircleNum(self, M: List[List[int]]) -> int:
        length = len(M)
        visited = [0]*length

        def dfs(x: int):
            visited[x] = 1
            for y in range(length):
                if not visited[y] and M[x][y]:
                    dfs(y)
        res = 0
        for x in range(length):
            if not visited[x]:
                res += 1
                dfs(x)
        return res

    def findCircleNum(self, M: List[List[int]]) -> int:
        length = len(M)
        visited = [0]*length

        def bfs(x: int):
            queue = [x]
            while queue:
                queue = [
                    y for x in queue for y in range(length) if not visited[y] and M[x][y]
                ]
                for x in queue:
                    visited[x] = 1

        res = 0
        for x in range(length):
            if not visited[x]:
                res += 1
                bfs(x)
        return res
# @lc code=end
