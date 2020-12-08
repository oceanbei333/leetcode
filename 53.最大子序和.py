#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 用 index_max_num 代表以第 i 个数结尾的「连续子数组的最大和」
        max_num = index_max_num = nums[0]
        for val in nums[1:]:
            index_max_num = max(index_max_num+val, val)
            max_num = max(index_max_num, max_num)
        return max_num


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for index in range(1, len(nums)):
            if nums[index-1] > 0:
                nums[index] += nums[index-1]
        return max(nums)


# @lc code=end
