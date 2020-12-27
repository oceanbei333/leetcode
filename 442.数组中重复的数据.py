#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        return [nums[i] for i in range(len(nums)-1) if nums[i] == nums[i+1]]
        
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) -1
            if nums[index]<0:
                res.append(abs(nums[i]))
            else:
                nums[index] *= -1
        return res
# @lc code=end
