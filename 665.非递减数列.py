#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for index in range(1, len(nums)):
            if nums[index-1] > nums[index]:
                if index > 1 and nums[index - 2] > nums[index]:
                    nums[index] = nums[index-1]
                count += 1
            if count > 1:
                return False
        return True
# @lc code=end
