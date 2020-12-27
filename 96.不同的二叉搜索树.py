#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        # 相同长度的二叉搜索树的数量相同
        if n < 2:
            return 1
        return sum(self.numTrees(j-1)*self.numTrees(n-j) for j in range(1, n+1))

    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]

    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def dp(start: int, end: int):
            if start >= end:
                return 1
            return sum(dp(start, i-1)*dp(i+1, end) for i in range(start, end+1))
        return dp(1, n)

    def numTrees(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        for length in range(1, n+1):
            for start in range(n-length+1):
                end = start + length - 1
                for i in range(start, end+1):
                    dp[start][end] += (dp[start][i-1] or 1)*(dp[i+1][end] or 1)
        return dp[0][n-1]

# @lc code=end
