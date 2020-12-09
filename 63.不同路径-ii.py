#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List, overload


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        @functools.lru_cache(None)
        def dp(x: int, y: int) -> int:
            if x >= n or y >= m or obstacleGrid[x][y]:
                return 0
            if x == n-1 and y == m-1:
                return 1
            return dp(x+1, y)+dp(x, y+1)
        return dp(0, 0)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[0][1] = 1
        for x in range(1, n+1):
            for y in range(1, m+1):
                if not obstacleGrid[x-1][y-1]:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[0][-1] = 1
        for x in range(n):
            for y in range(m):
                if not obstacleGrid[x][y]:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[-2][-2]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        pre_col = [0]*(m+1)
        pre_col[0] = 1
        for x in range(n):
            for y in range(m):
                if not obstacleGrid[x][y]:
                    pre_col[y] += pre_col[y-1]
                else:
                    pre_col[y] = 0
        return pre_col[-2]
# @lc code=end
