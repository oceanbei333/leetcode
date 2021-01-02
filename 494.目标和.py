#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(None)
        def dp(count: int, target: int):
            if not count and not target:
                return 1
            if count < 1:
                return 0
            return dp(count-1, target-nums[count-1]) + dp(count-1, target+nums[count-1])
        return dp(len(nums), S)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        max_ = sum(nums)
        from collections import defaultdict
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for target in range(-max_, max_+1):
                dp[i][target] += dp[i-1][target-nums[i-1]]
                dp[i][target] += dp[i-1][target+nums[i-1]]
        return dp[n][S]

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        max_ = sum(nums)
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        pre = dp.copy()
        for i in range(1, n+1):
            for target in range(-max_, max_+1):
                dp[target] = pre[target-nums[i-1]] + pre[target+nums[i-1]]
            pre = dp.copy()
        return dp[S]

# @lc code=end
