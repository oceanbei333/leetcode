#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i]+= nums[i-1]
        return max(nums)

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum= sum_ = nums[0]
        for val in nums[1:]:
            sum_ = max(sum_+val, val)
            max_sum = max(max_sum, sum_)
        return max_sum
# @lc code=end
