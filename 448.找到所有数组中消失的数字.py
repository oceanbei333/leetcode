#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        aset = set(nums)
        return [val for val in range(1, len(nums)+1) if val not in aset]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            nums[abs(nums[index])-1] = -abs(nums[abs(nums[index])-1])
        alist = []
        for index, val in enumerate(nums):
            if val > 0:
                alist.append(index+1)
        return alist

# @lc code=end
