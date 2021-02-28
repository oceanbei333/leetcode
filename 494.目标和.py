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
            if not count :
                if not target:
                    return 1
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

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)+S
        if total%2:
            return 0
        n = len(nums)
        total >>= 1
        dp = [[0]*(total+1) for _ in range(n+1)]
        for count in range(n+1):
            dp[count][0] = 1
        for count in range(1, n+1):
            for target in range(1, total+1):
                dp[count][target] = dp[count-1][target] + dp[count-1][target-nums[count-1]]
        return dp[n][total]

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)+S
        if total%2:
            return 0
        n = len(nums)
        total >>= 1
        dp = [0]*(total+1)
        dp[0] = 1
        for count in range(1, n+1):
            for target in range(total,0, -1):
                dp[target] = dp[target] + dp[target-nums[count-1]]
        return dp[total]
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)+S
        if total%2:
            return 0
        n = len(nums)
        target = total >> 1
        @lru_cache(None)
        def backtrack(count:int, target:int):
            if not count:
                if not target:
                    return 1
                return 0
            return backtrack(count-1, target) + backtrack(count-1, target-nums[count-1])
        return backtrack(n, target)


# @lc code=end
