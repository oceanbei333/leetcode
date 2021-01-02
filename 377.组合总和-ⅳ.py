#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(target: int):
            if not target:
                return 1
            if target < 0:
                return 0
            return sum(dp(target-num) for num in nums)
        return dp(target)

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(target: int):
            if not target:
                return 1
            if target < 0:
                return 0
            return sum(dfs(target-num) for num in nums)
        return dfs(target)

# @lc code=end
