#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(1, len(nums)):
            if nums[index-1] == nums[index]:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        aset = set()
        for val in nums:
            if val in aset:
                return True
            else:
                aset.add(val)
        return False


# @lc code=end
