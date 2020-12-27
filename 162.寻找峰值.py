#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(float('-inf'))
        for i in range(n):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i

    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(float('-inf'))
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid-1] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return r
# @lc code=end
