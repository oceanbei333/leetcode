#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        target = length - 1
        for i in range(length-1, -1, -1):
            if nums[i] + i >= target:
                target = i
        return not target

    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        end = 0
        for i in range(length):
            if i <= end:
                if i + nums[i] >= length-1:
                    return True
                end = max(end, i+nums[i])
        return False


# @lc code=end
