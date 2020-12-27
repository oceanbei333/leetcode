#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = 0
        for i in range(n):
            if not nums[i]:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
        p1 = p0
        for i in range(p1, n):
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1

    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif not nums[i]:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2, i = 0, n-1, 0
        while i <= p2:
            while i<=p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if not nums[i]:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0+=1
            i+=1
            



# @lc code=end
