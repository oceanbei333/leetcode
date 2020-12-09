#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
from typing import List, Set, Tuple


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        unvisited_set = set()
        start_x, start_y = 0, 0
        for x in range(n):
            for y in range(m):
                if not grid[x][y]:
                    unvisited_set.add((x, y))
                elif grid[x][y] == 1:
                    start_x, start_y = x, y
                    unvisited_set.add((x, y))

        def dp(x: int, y: int, unvisited_set: Set[Tuple[int, int]]) -> int:
            if not (0 <= x < n and 0 <= y < m):
                return 0
            if grid[x][y] == -1:
                return 0
            if grid[x][y] == 2 and not unvisited_set:
                return 1
            if (x, y) not in unvisited_set:
                return 0
            unvisited_set = unvisited_set.copy()
            unvisited_set.remove((x, y))
            return (
                dp(x+1, y, unvisited_set) +
                dp(x, y+1, unvisited_set) +
                dp(x-1, y, unvisited_set) +
                dp(x, y-1, unvisited_set)
            )
        return dp(start_x, start_y, unvisited_set)

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        unvisited_set = {(x, y) for x in range(n)
                         for y in range(m) if not grid[x][y] or grid[x][y]==1}

        def dfs(x: int, y: int, grid: List[List[int]]) -> int:
            if not (0 <= x < n and 0 <= y < m):
                return 0
            val = grid[x][y]
            if val == -1:
                return 0
            if val == 2 and not unvisited_set:
                return 1
            if (x, y) not in unvisited_set:
                return 0
            grid[x][y] = -1
            unvisited_set.remove((x, y))
            steps = dfs(x+1, y, grid) + dfs(x, y+1, grid) + \
                dfs(x-1, y, grid) + dfs(x, y-1, grid)
            grid[x][y] = val
            unvisited_set.add((x, y))
            return steps
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    return dfs(x, y, grid)
# @lc code=end
