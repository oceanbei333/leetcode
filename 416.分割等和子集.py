#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total >> 1
        n = len(nums)

        @lru_cache(None)
        def dp(count: int, target: int) -> bool:
            if not target:
                return True
            if target < 0 or count < 1:
                return False
            return dp(count-1, target-nums[count-1]) or dp(count-1, target)
        return dp(n, target)

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total >> 1
        n = len(nums)
        dp = [[False]*(total+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                if j-nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        return dp[n][target]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total >> 1
        n = len(nums)
        dp = [False]*(target+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(target, nums[i-1]-1, -1):
                dp[j] |= dp[j-nums[i-1]]
        return dp[target]
# @lc code=end
