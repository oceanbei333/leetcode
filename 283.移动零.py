#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[count] = nums[i]
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = []
        non_zeros = []
        for num in nums:
            if num:
                non_zeros.append(num)
            else:
                zeros.append(num)
        nums[:] = non_zeros+zeros
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[count] = nums[i]
                if i!=count:
                    nums[i] = 0
                count += 1
# @lc code=end

