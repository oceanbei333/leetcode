#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = dict()
        for index in range(len(nums)):
            another_num = target - nums[index]
            if another_num in adict:
                return [adict[another_num], index]
            else:
                adict[nums[index]] = index

# @lc code=end
