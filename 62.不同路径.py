#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.lru_cache(None)
        def _uniquePaths(x: int, y: int) -> int:
            if x >= m or y >= n:
                return 0
            if x == m-1 and y == n-1:
                return 1
            return _uniquePaths(x+1, y) + _uniquePaths(x, y+1)
        return _uniquePaths(0, 0)

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][1] = 1
        for x in range(1, m+1):
            for y in range(1, n+1):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        pre_col = [0]*(n+1)
        pre_col[0] = 1
        cur_col = [0]*(n+1)
        for _ in range(m):
            for y in range(n):
                cur_col[y] = pre_col[y] + cur_col[y-1]
            pre_col = cur_col
        return pre_col[-2]

    def uniquePaths(self, m: int, n: int) -> int:
        pre_col = [1]+[0]*n
        for _ in range(m):
            for y in range(n):
                pre_col[y] += pre_col[y-1]
        return pre_col[-2]

    def uniquePaths(self, m: int, n: int) -> int:
        pre_col = [1]*n
        for _ in range(1, m):
            for y in range(1, n):
                pre_col[y] += pre_col[y-1]
        return pre_col[-1]


# @lc code=end
