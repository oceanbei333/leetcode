#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        @functools.lru_cache(None)
        def dp(x: int, y: int) -> int:
            if x < 0 or y < 0:
                return float('inf')
            if not x and not y:
                return grid[0][0]
            return min(dp(x-1, y), dp(x, y-1)) + grid[x][y]
        return dp(n-1, m-1)

    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')]*(m+1) for _ in range(n+1)]
        dp[0][-1] = 0
        for x in range(n):
            for y in range(m):
                dp[x][y] = min(dp[x][y-1], dp[x-1][y]) + grid[x][y]
        return dp[-2][-2]

    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        pre_col = [float('inf')]*(n+1)
        for y in range(m):
            for x in range(n):
                if not x and not y:
                    pre_col[x] = grid[0][0]
                else:
                    pre_col[x] = min(pre_col[x], pre_col[x-1])+grid[x][y]
        return pre_col[-2]


# @lc code=end
