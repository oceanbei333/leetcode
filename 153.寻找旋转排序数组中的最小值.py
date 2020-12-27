#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        if nums[0] < nums[-1]:
            return nums[0]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                if nums[mid] > nums[0]:
                    l = mid+1
                else:
                    r = mid - 1

# @lc code=end
