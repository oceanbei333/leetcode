#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int((n+1)*n/2) - sum(nums)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]:
            return 0
        if nums[-1] != len(nums):
            return len(nums)
        for index in range(1, len(nums)):
            if nums[index] - 1 != nums[index-1]:
                return nums[index] - 1


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        adict = {val for val in nums}
        for val in range(len(nums)+1):
            if val not in adict:
                return val


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = len(nums)
        for index, val in enumerate(nums):
            missing_num ^= val ^ index
        return missing_num

# @lc code=end
