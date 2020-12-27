#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c]:
                grid[r][c] = 0
                return dfs(r+1, c)+dfs(r, c+1)+dfs(r-1, c)+dfs(r, c-1)+1
            return 0
        return max(dfs(r, c) for r in range(rows) for c in range(cols))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        f = dict()

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = f[find(y)]

        rows = len(grid)
        cols = len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    find((r, c))
                    if r+1 < rows and grid[r+1][c]:
                        union((r, c), (r+1, c))
                    if c+1 < cols and grid[r][c+1]:
                        union((r, c), (r, c+1))
        from collections import defaultdict
        count = defaultdict(int)
        count[(-1, -1)] = 0
        for key in f:
            count[find(key)] += 1
        return max(count.values())


# @lc code=end
