#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(start: int, end: int, turn: int) -> int:
            if start > end:
                return 0
            s_start = nums[start]*turn + dp(start+1, end, -turn)
            s_end = nums[end]*turn + dp(start, end-1, -turn)
            if turn == 1:
                return max(s_start, s_end)
            else:
                return min(s_start, s_end)
        return dp(0, len(nums)-1, 1) >= 0

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n, -1, -1):
            for j in range(i, n):
                dp[i][j] = max(
                    nums[i] - dp[i + 1][j],
                    nums[j] - dp[i][j - 1]
                )
        return dp[0][n - 1] >= 0
# @lc code=end
