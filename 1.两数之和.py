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
        for i in range(len(nums)):
            if target-nums[i] in adict:
                return [adict[target-nums[i]],i]
            adict[nums[i]] = i
# @lc code=end
