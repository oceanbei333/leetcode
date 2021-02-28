#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
    def integerBreak(self, n: int) -> int:
        if n<4:
            return n-1
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = max(2*(i-2), 2*dp[i-2], 3*(i-3), 3*dp[i-3])
        return dp[n]

# @lc code=end
