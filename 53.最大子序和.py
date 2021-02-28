#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(n:int):
            if not n:
                return nums[0]
            return helper(n-1) + nums[n] if helper(n-1) >0 else nums[n]
        return max(helper(i) for i in range(len(nums)))


    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        # 以i结尾的子序列的最大和
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i-1]+nums[i] if dp[i-1] > 0 else nums[i]
        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = cur = nums[0]
        for i in range(1, n):
            cur = cur+nums[i] if cur > 0 else nums[i]
            max_ = max(cur, max_)
        return max_

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# @lc code=end
