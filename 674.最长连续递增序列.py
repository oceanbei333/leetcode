#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        @functools.lru_cache(len(nums))
        def dp(index: int):
            if not index:
                return 1
            if nums[index] > nums[index-1]:
                return dp(index-1)+1
            return 1
        if not nums:
            return 0
        return max(dp(i) for i in range(len(nums)))

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1]*l
        for i in range(1, l):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1]+1
        dp.append(0)
        return max(dp)

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res, cur = 0, 0
        nums.append(float('-inf'))
        for i in range(len(nums)):
            if nums[i] > nums[i-1]:
                cur = cur+1
                res = max(res, cur)
            else:
                cur = 1
        return res

# @lc code=end
