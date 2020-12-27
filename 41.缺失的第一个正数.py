#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in sorted(set(nums)) if num > 0]
        if not nums:
            return 1
        for num in range(1, len(nums)+1):
            if num != nums[num-1]:
                return num
        return nums[-1]+1

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        for i in range(n):
            val = abs(nums[i])
            if val < n+1:
                nums[val-1] = -abs(nums[val-1])
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1


# @lc code=end
